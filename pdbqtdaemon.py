import re
import sys,time,os
from daemon import Daemon

class PDBQTDaemon(Daemon):
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
		self.count = 1

	def prepare(self, id, templ):
		pass

	def resume(self,  id):
		pass

	def jCount(self):
		os.system('squeue -u {} -n {} | wc > {}'.format(self.user, self.proc_name, self.path.squeue_stats(self.proc_name)))
		tpl = open(self.path.squeue_stats(self.proc_name)).read().strip()
		tpl = re.split('\s+',tpl)

		return int(tpl[0])-1

	def hold(self):
		jc = self.jCount()
		while jc > 0:
			print('holding ... {} jobs'.format(jc))
			time.sleep(self.hold_time)
			jc = self.jCount()
		

	def molecule_done(self, id):
		pass

	def process_molecule(self, id):
		if self.molecule_done(id):
			return False

		if self.count % self.payload == 0:
			self.hold()

		self.prepare(id, self.template)

		os.system(self.command)

		self.resume(id)

		print('{}'.format(id))

		self.count += 1

	def run(self):
		while self.count > 0:
			self.db.foreachId(
				lambda id: self.process_molecule(id)
			)
			self.count = 0

		self.db.close()


	def restart(self):
		self.count = 1
		Daemon.restart(self)

	def stop(self):
		self.db.close()
		Daemon.stop(self)