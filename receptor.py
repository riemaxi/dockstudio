from molecule import Molecule

class Receptor(Molecule):
	def __init__(self, name):
		Molecule.__init__(self,name,1)
		self.location = self.getMaxEntityId() + 1

	def add(self,id):
		Molecule.pushEntity(self, self.location, [(0, id)])
		self.location += 1
