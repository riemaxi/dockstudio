import os
from pdbqtdaemon import PDBQTDaemon
from parameter import Parameter
from receptor import Receptor
from path import Path

process_name = 'prepare_receptor'

p = Parameter()
pt = Path(p)
user = p._('user')
payload = p.i('daemon.sbatch.payload')
db = Receptor(pt.receptordb)

class PrepareReceptor(PDBQTDaemon):
	def __init__(self):
		PDBQTDaemon.__init__(self,
					user,
					db,
					pt,
					payload,
					process_name)

	def molecule_done(self, id):
		return os.path.isfile(pt.receptorpdbqt(id))


	def prepare(self, id, templ):
		os.chdir(self.path.docking_receptor)

		log_name = '{}/{}_{}.out'.format(self.path.log, self.proc_name, id)
		templ = self.template.format(log_name, self.path.receptor(id), id)
		target = '{}_{}.sbatch'.format(id, self.proc_name)
		open(target, 'w').write(templ)

		self.command = 'sbatch ' + target
	
		PDBQTDaemon.prepare(self, id, templ)

	def resume(self, id):
		target = '{}_{}.sbatch'.format(id, self.proc_name)
		os.system('rm -f {}'.format(target) )

		PDBQTDaemon.resume(self, id)
		
