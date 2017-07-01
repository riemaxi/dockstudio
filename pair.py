from ligand import Ligand
from receptor import Receptor

class Pair:
	def __init__(self, receptordb, liganddb):
		self.ligand = Ligand(liganddb)
		self.receptor = Receptor(receptordb)


	def foreachPair(self, pid, sink):
		self.ligand.foreachId(
			lambda cid: sink(pid, cid)
		)

	def foreach(self, sink, criteria = ''):
		self.receptor.foreachId(
			lambda pid: self.foreachPair( pid, sink)
		)

	def size(self, rcriteria = '1=1', lcriteria = '1=1'):
		ligands = self.ligand.size(lcriteria)
		receptors = self.receptor.size(rcriteria)
		return ligands * receptors

	def close(self):
		self.ligand.close()
		self.receptor.close()

