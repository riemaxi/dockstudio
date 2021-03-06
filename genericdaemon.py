import re
import sys,time,os
from daemon import Daemon

class GenericDaemon(Daemon):
	def __init__(self,user, db, path,  payload = 450, proc_name='job', hold_time = 10):
		Daemon.__init__(self,
			path.pidfile(proc_name),
			stdout = path.stdout(proc_name),
			stderr = path.stderr(proc_name))

		self.path = path
		self.user = user
		self.db = db
		self.payload = payload
		self.proc_name = proc_name
		self.command = 'sbatch ' + self.path.job_script(self.proc_name)
		self.hold_time = hold_time
		self.template = open(self.path.job_template(self.proc_name)).read()
		self.count = 1

	def prepare(self,dir, cid, pid, templ):
		open(self.path.job_script(self.proc_name), 'w').write( templ)

	def resume(self, dir, cid, pid):
		pass

	def jCount(self):
		os.system('squeue -u {} -n {} | wc > {}'.format(self.user, self.proc_name, self.path.squeue_stats))
		tpl = open(self.path.squeue_stats).read().strip()
		tpl = re.split('\s+',tpl)

		return int(tpl[0])-1

	def hold(self):
		jc = self.jCount()
		while jc > 0:
			print('holding ... {} jobs'.format(jc))
			time.sleep(self.hold_time)
			jc = self.jCount()
		

	def process_pair(self, pid, cid):
		if os.path.isfile(self.path.pair_done(pid, cid)):
			return False

		if self.count % self.payload == 0:
			self.hold()

		dir = self.path.pairdir(pid,cid)

		os.chdir(dir)
		self.prepare(dir, cid, pid, self.template)

		os.system(self.command)

		self.resume(dir, cid, pid)
		os.chdir(self.path.root)

		print('{}\t{}'.format(cid,pid))

		self.count += 1

	def run(self):
		while self.count > 0:
			self.count = 0
			self.db.foreach(
				lambda pid, cid: self.process_pair(pid, cid)
			)
		self.db.close()
		os.system( 'touch {}'.format(self.path.all_done) )


	def restart(self):
		self.count = 1
		Daemon.restart(self)

	def stop(self):
		self.db.close()
		Daemon.stop(self)
