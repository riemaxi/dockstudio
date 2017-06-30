from valid import Domain

class Molecule(Domain):
	def __init__(self, name, domain = 0):
		Domain.__init__(self, name, domain)

	def add(self, id):
		pass

	def rem(self, ids):
		Domain.rem(self, 'id in ({})'.format(ids))
