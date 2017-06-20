import os

class Path:
	def __init__(self, p):
		self.root = p._('root', os.getcwd())
		self.project = self.root + '/project/'
		self.dir = self.project + p._('project.wizard.create.name')
		self.data = self.dir + '/data/'
		self.docking = self.dir + '/docking/'
		self.pairdb = self.data + p._('project.wizard.pair.db')
		self.receptordb = self.data + p._('project.wizard.receptor.db')
		self.liganddb = self.data + p._('project.wizard.ligand.db')

	def pairdir(self, pid, cid):
		return self.docking + '{}_{}'.format(pid, cid)
