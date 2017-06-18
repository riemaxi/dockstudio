import urllib.request as Ureq
from molecule import Molecule

class Receptor(Molecule):
	STRUCTURE_URL = 'https://files.rcsb.org/download/{}.pdb'
	STRUCTURE_FORMAT = 'pdb'

	def __init__(self, name):
		Molecule.__init__(self,name)
		self.location = self.getMaxEntityId() + 1

	def add(self,id):
		Molecule.pushEntity(self, self.location, [(0, id)])
		self.location += 1

	def fetch(self, id):
		url = self.STRUCTURE_URL.format(id)
		try:
			req = Ureq.Request(url)
			with Ureq.urlopen(req) as resp:
				return resp.read().decode('utf8')
		except:
			return url

	def foreachStructure(self, sink):
		Molecule.foreach(
			self,
			lambda data: sink(data[1][1], self.fetch(data[1][1]), self.STRUCTURE_FORMAT)
		)
