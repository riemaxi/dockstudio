import os
from genericdaemon import GenericDaemon
from parameter import Parameter
from pair import Pair
from path import Path

p = Parameter()
pt = Path(p)
user = p._('user')
payload = p.i('daemon.sbatch.payload')

proc_name = 'prepare_ligand'

class PrepareLigand(GenericDaemon):
	def __init__(self):
		GenericDaemon.__init__(self,
					user,
					pt.root, 
					pt.pairdb,
					pt.docking,
					payload,
					process_name)

	def prepare(self, dir, cid, pid):
		pass
