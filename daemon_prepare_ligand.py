import os
from pdbqtdaemon import PDBQTDaemon
from parameter import Parameter
from ligand import Ligand
from path import Path

process_name = 'prepare_ligand'

p = Parameter()
pt = Path(p)
user = p._('user')
payload = p.i('daemon.sbatch.payload')
db = Ligand(pt.liganddb)

class PrepareLigand(PDBQTDaemon):
	def __init__(self):
		PDBQTDaemon.__init__(self,
					user,
					db,
					pt,
					payload,
					process_name)

	def molecule_done(self, id):
		return os.path.isfile(pt.ligandpdbqt(id))


	def prepare(self, id, templ):
		os.chdir(self.path.docking_ligand)

		log_name = '{}/{}_{}.out'.format(self.path.log, self.proc_name, id)
		templ = self.template.format(log_name, self.path.ligand(id), id)
		target = '{}_{}.sbatch'.format(id, self.proc_name)
		open(target, 'w').write(templ)

		self.command = 'sbatch ' + target
	
		PDBQTDaemon.prepare(self, id, templ)

	def resume(self, id):
		target = '{}_{}.sbatch'.format(id, self.proc_name)
		os.system('rm -f {}'.format(target) )

		PDBQTDaemon.resume(self, id)
		
