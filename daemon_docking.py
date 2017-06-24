import sys
import os
from pairdaemon import PairDaemon
from parameter import Parameter
from path import Path
from pair import Pair

process_name = 'docking'

p = Parameter()
pt = Path(p)
user = p._('user')
payload = p.i('daemon.sbatch.payload')
db = Pair(pt.receptordb, pt.liganddb)

class Docking(PairDaemon):
	def __init__(self):
		PairDaemon.__init__(self,
					user,
					db,
					pt,
					payload,
					process_name)

	def step_done(self, pid, cid):
		mapfile = pt.pairdir(pid, cid) + '/scoring.log'
		return os.path.isfile(mapfile)


	def adapt_parameter_file(self):
		target = 'ligand_receptor.dpf'
		names = [
			'autodock_parameter_version',
			'outlev',
			'intelec',
			'ligand_types',
			'fld',
			'map',
			'elecmap',
			'desolvmap',
			'move',
			'about']

		template = ''
		for line in open(target):
			name  = line.split(' ')
			if name[0] in names:
				template += line

		template += open(self.path.docking_template).read()

		with open(target,'w') as file:
			file.write(template + '\n')


	def prepare(self,  pid, cid, templ):
		dir = self.path.pairdir(pid, cid)
		os.chdir(dir)

		self.adapt_parameter_file()

		log_name = '{}/{}_{}_{}.out'.format(self.path.log, self.proc_name, pid,cid)
		templ = self.template.format(log_name)
		target = '{}_{}.sbatch'.format(self.path.project_name, self.proc_name)
		open(target, 'w').write(templ)

		self.command = 'sbatch ' + target
	
		PairDaemon.prepare(self, pid, cid, templ)

	def resume(self, pid, cid):
		target = '{}_{}.sbatch'.format(self.path.project_name, self.proc_name)
		os.system('rm -f {}'.format(target) )

		PairDaemon.resume(self, pid, cid)

