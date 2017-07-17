import re
import sys,time,os
from daemon import Daemon

class PairDaemon(Daemon):
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
		self.hold_time = hold_time
		self.template = open(self.path.job_template(self.proc_name)).read()

	def prepare(self, pid, cid, templ):
		pass

	def resume(self, cid, pid):
		pass

	def jCount(self):
		os.system("squeue -t R -u {} --Format=name | grep -e '{}_{}' | wc > {}".format(self.user, self.path.project_name, self.proc_name, self.path.squeue_stats(self.proc_name)))
		tpl = open(self.path.squeue_stats(self.proc_name)).read().strip()
		tpl = re.split('\s+',tpl)

		count = int(tpl[0])
		print('squeue running jobs: ',count)
		return count

	def hold(self):
		jc = self.jCount()
		while jc > 10:
			print('holding ... {} jobs'.format(jc))
			time.sleep(self.hold_time)
			jc = self.jCount()
		
	def step_done(self, pid, cid):
		pass

	def process_pair(self, pid, cid):
		if self.step_done(pid, cid):
			self.count -= 1
			return False

		if self.index % self.payload == 0:
			self.hold()

		self.prepare(pid, cid, self.template)

		os.system(self.command)

		self.resume(pid, cid)

		print('{}\t{}'.format(pid,cid))

		self.count -= 1
		self.index += 1


	def run(self):
		self.count = self.db.size()
		while self.count > 0:
			self.index = 1
			self.db.foreach(
				lambda pid, cid: self.process_pair(pid, cid)
			)

		self.db.close()

	def restart(self):
		Daemon.restart(self)

	def stop(self):
		self.db.close()
		Daemon.stop(self)
