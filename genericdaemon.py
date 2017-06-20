import re
import sys,time,os
from daemon import Daemon

class GenericDaemon(Daemon):
	def __init__(self,user, root, db, dock_dir, payload = 450, proc_name='job', squeue_file='squeue.txt', hold_time = 10, log = 'log'):
		Daemon.__init__(self,
			root + 'log/daemon_' + proc_name + '.pid',
			stdout = root + log + ' /daemon_' + proc_name + '.txt',
			stderr = root + log + '/daemon_' + proc_name + '_error.txt')

		self.user = user
		self.root = root
		self.db = db
		self.dock_dir = dock_dir
		self.payload = payload
		self.proc_name = proc_name
		self.proc_name_script = proc_name + '.sh'
		self.squeue_file = root + log + '/' + proc_name + '_' + squeue_file
		self.command = 'sbatch ' + self.proc_name_script
		self.hold_time = hold_time
		self.template = open(root + 'template/' + self.proc_name_script).read()
		self.count = 1

	def prepare(self,dir, cid, pid):
		open(self.root + dir + self.proc_name_script, 'w').write( self.template )

	def resume(self, dir, cid, pid):
		pass

	def jCount(self):
		os.system('squeue -u {} -n {} | wc > {}'.format(self.user, self.proc_name, self.squeue_file))
		tpl = open(self.squeue_file).read().strip()
		tpl = re.split('\s+',tpl)

		return int(tpl[0])-1

	def hold(self):
		jc = self.jCount()
		while jc > 0:
			print('holding ... {} jobs'.format(jc))
			time.sleep(self.hold_time)
			jc = self.jCount()
		

	def process_pair(self, cid, pid):
		dir = '{}/{}_{}/'.format(self.dock_dir,cid,pid)


		os.chdir(dir)
		self.prepare(dir, cid, pid)

		os.system(self.command)

		self.resume(dir, cid, pid)
		os.chdir(self.root)

		print('{}\t{}'.format(cid,pid))

	def process(self, cid, data):
		dir = self.dock_dir
		for cell in data:
			pid, state = cell[1].split(':')
			path = '{}/{}_{}/{}.done'.format(dir, cid, pid, self.proc_name)
			if not os.path.isfile(path):
				if self.count % self.payload == 0:
					self.hold()

				self.process_pair(cid,pid)
				self.count += 1


	def run(self):
		while self.count>0:
			self.count = 0
			self.db.foreach(
				lambda cid, data: self.process(cid, data)
			)
		self.db.close()
		os.system( 'touch {}/{}.done'.format(self.dir, self.proc_name) )


	def restart(self):
		self.count = 1
		Daemon.restart(self)

	def stop(self):
		self.db.close()
		Daemon.stop(self)
