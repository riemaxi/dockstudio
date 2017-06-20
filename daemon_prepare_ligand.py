import os
from genericdaemon import GenericDaemon
from parameter import Parameter
from progress import Progress

p = Parameter()
root = p._('root')
user = p._('user')
payload = p.i('daemon.sbatch.payload')

proc_name = 'prepare_ligand'

class PrepareLigand(GenericDaemon):
	def __init__(self, db, dir):
		GenericDaemon.__init__(self,
					user,
					root, 
					db,
					dir,
					payload,
					process_name)

	def prepare(self, dir, cid, pid):
		pass
