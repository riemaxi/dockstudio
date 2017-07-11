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
		id = id.strip()
		if len(id):
			Molecule.pushEntity(self, id, [(0, id)])

	def fetch(self, id, sink, download, other):
		if download != None and download(id):
			url = self.STRUCTURE_URL.format(id)
			try:
				req = Ureq.Request(url)
				with Ureq.urlopen(req) as resp:
					sink(id, resp.read().decode('utf8'), self.STRUCTURE_FORMAT)
			except OSError as e:
				sink(id, None, None)
		else:
			other(id)

	def foreachStructure(self, sink, download = None, other = None):
		Molecule.foreach(
			self,
			lambda data: self.fetch(data[0][1], sink, download, other )
		)

	def getData(self, r, columns):
		data = []
		for item in r:
			if item['urn'].get('label','') in columns:
				val = item['value'].get('sval', item['value'].get('ival', item['value'].get('fval'))) 
				data.append(str(val).strip())

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
