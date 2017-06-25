import xml.etree.ElementTree as xtree
import urllib.request as Ureq
from molecule import Molecule

class Receptor(Molecule):
	RECORD_URL = 'http://www.rcsb.org/pdb/rest/customReport.xml?pdbids={0}&customReportColumns={1}&format=xml&service=wsfile'
	STRUCTURE_URL = 'https://files.rcsb.org/download/{}.pdb'
	STRUCTURE_FORMAT = 'pdb'

	def __init__(self, name):
		Molecule.__init__(self,name)
		self.location = self.getMaxEntityId() + 1

	def add(self,id):
		Molecule.pushEntity(self, self.location, [(0, id)])
		self.location += 1

	def fetchStructure(self, id, download, sink, other):
		if download != None and download(id):
			url = self.STRUCTURE_URL.format(id)
			try:
				req = Ureq.Request(url)
				with Ureq.urlopen(req) as resp:
					sink(id, resp.read().decode('utf8'), self.STRUCTURE_FORMAT)
			except:
				sink(id, None, None)
		else:
			if other != None:
				other(id)

	def foreachStructure(self, sink, download = True, other = None):
		Molecule.foreach(
			self,
			lambda data: self.fetchStructure(data[1][1], download,sink, other)
		)

	def fetchRecord(self, id, columns, colist):
		url = self.RECORD_URL.format(id, columns)
		req = Ureq.Request(url)

		data = ''
		for chunck in Ureq.urlopen(req):
			data += chunck.decode('utf8')
		data = xtree.fromstring(data)
		lst = data.findall('record')

		fields = []
		for record in lst:
			for name in colist:
				fields.append(record.find('dimStructure.' + name).text)

		return  '\t'.join(fields)


	def foreachRecord(self, columns, sink):
		colist = columns.split(',')
		Molecule.foreach(
			self,
			lambda data: sink(data[1][1], self.fetchRecord(data[1][1], columns, colist) )
		)

	def foreachId(self, sink):
		Molecule.foreach(
			self,
			lambda data: sink( data[1][1] )
		)
