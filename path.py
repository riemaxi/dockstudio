import os

class Path:
	def __init__(self, p):
		self.root = p._('root', os.getcwd())
		self.project = self.root + '/project/'
		self.project_name = p._('project.wizard.create.name')
		self.dir = self.project + self.project_name
		self.template = self.project + 'template/'
		self.docking_template = self.template + 'docking_param.txt'
		self.data = self.dir + '/data/'
		self.log = self.dir + '/log'
		self.docking = self.dir + '/docking/'
		self.pairdb = self.data + p._('project.wizard.pair.db')
		self.receptordb = self.data + p._('project.wizard.receptor.db')
		self.liganddb = self.data + p._('project.wizard.ligand.db')
		self.docking_ligand = self.docking + 'ligand'
		self.docking_receptor = self.docking + 'receptor'

	def clear(self, proc_name):
		os.system('rm -f ' + self.pidfile(proc_name))
		os.system('rm -f ' + self.stdout(proc_name))
		os.system('rm -f ' + self.stderr(proc_name))
		os.system('rm -f ' + self.squeue_stats(proc_name))
		os.system('rm -f {}/{}_*.out'.format(self.log, proc_name))


	def pairdir(self, pid, cid):
		return self.docking + '{}_{}'.format(pid, cid)

	def pair_done(self, proc, pid, cid):
		return '{}/done/{}_{}_{}.done'.format(self.dir, proc, pid, cid)

	
	def all_done(self, proc_name):
		return self.docking + 'done/{}.done'.format(proc_name)


	def pidfile(self, proc_name):	
		return '{}/daemon_{}.pid'.format(self.log, proc_name)

	def stdout(self, proc_name):
		return '{}/daemon_out_{}.txt'.format(self.log, proc_name)


	def stderr(self, proc_name):
		return '{}/daemon_err_{}.txt'.format(self.log, proc_name)

	def squeue_stats(self, proc_name):
		return '{}/squeue_stats_{}.txt'.format(self.log, proc_name)


	def script(self, proc_name):
		return '{}script/{}.sbatch'.format(self.project, self.proc_name)


	def pair_script(self, pid, cid,  proc_name):
		return '{}/{}.sbatch'.format(self.pairdir(pid, cid), self.proc_name)

	def job_template(self, proc_name):
		return '{}template/{}.sbatch'.format(self.project, proc_name)


	def ligand(self, id):
		return '{}structure/ligand/{}.pdb'.format(self.data, id )

	def ligandpdbqt(self, id):
		return '{}ligand/{}.pdbqt'.format(self.docking, id )


	def receptor(self, id):
		return '{}structure/receptor/{}.pdb'.format(self.data, id )

	def receptorpdbqt(self, id):
		return '{}receptor/{}.pdbqt'.format(self.docking, id )
