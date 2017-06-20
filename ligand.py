import urllib.request as Ureq
from molecule import Molecule
import json

class Ligand(Molecule):
	RECORD_URL = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{}/record/json'
	STRUCTURE_URL = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{}/sdf?record_type=3d'
	STRUCTURE_FORMAT = 'sdf'

	def __init__(self, name):
		Molecule.__init__(self, name)

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

	def getData(self, r, columns):
		data = []
		for item in r:
			if item['urn'].get('label','') in columns:
				val = item['value'].get('sval', item['value'].get('ival', item['value'].get('fval'))) 
				data.append(str(val))

		return data

	def fetchRecord(self, cid, columns):
		url = self.RECORD_URL.format(cid)
		req = Ureq.Request(url)
		r = json.loads(Ureq.urlopen(req).read().decode('utf8'))['PC_Compounds'][0]['props']

		data = self.getData(r, columns)

		return '\t'.join(data)

	def foreachRecord(self, columns, sink):
		Molecule.foreach(
			self,
			lambda data: sink(data[0][1], self.fetchRecord(data[0][1], columns) )
		)

	def foreachId(self, sink):
		Molecule.foreach(
			self,
			lambda data: sink( data[0][1] )
		)
