import urllib.request as Ureq
from molecule import Molecule

class Ligand(Molecule):
	STRUCTURE_URL = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{}/sdf?record_type=3d'
	STRUCTURE_FORMAT = 'sdf'

	def __init__(self, name):
		Molecule.__init__(self, name, 0)

	def add(self, id):
		Molecule.pushEntity(self, id, [(0, id)])

	def fetch(self, id):
		url = self.STRUCTURE_URL.format(id)
		try:
			req = Ureq.Request(url)
			with Ureq.urlopen(req) as resp:
				return resp.read().decode('utf8')
		except OSError as e:
			return e

	def foreachStructure(self, sink):
		Molecule.foreach(
			self,
			lambda data: sink(data[0][1], self.fetch(data[0][1]), self.STRUCTURE_FORMAT)
		)
