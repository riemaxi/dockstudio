from molecule import Molecule

class Ligand(Molecule):

	def __init__(self, name):
		Molecule.__init__(self, name, 0)

	def add(self, id):
		Molecule.pushEntity(self, id, [(0, id)])
