from valid import Domain

class Molecul√(Domain):
	RECEPTOR_DOM = 0
	LIGAND_DOM = 1

	def __init__(self, name):
		Domain.__init__(self, name)

	def addLigand(self, id):
		Domain.pushEntity(self, id, [(self.LIGAND_DOM, id)])

	def addReceptor(self,id, pid):
		Domain.pushEntity(self, id, [(self.RECEPTOR_DOM, pid)])
