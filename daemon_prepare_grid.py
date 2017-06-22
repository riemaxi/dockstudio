import sys
import os
from pairdaemon import PairDaemon
from parameter import Parameter
from path import Path

process_name = 'prepare_grid'

p = Parameter()
pt = Path(p)
user = p._('user')
payload = p.i('daemon.sbatch.payload')

class PrepareGrid(PairDaemon):
	def __init__(self):
		PairDaemon.__init__(self,
					user,
					None,
					pt,
					payload,
					process_name,
					stdin = sys.stdin)

	def step_done(self, pid, cid):
		return os.path.isdire(pt.pairdir(pid, cid))


	def prepare(self, dir,  pid, cid, templ):
		log_name = '{}/{}_{}_{}.out'.format(self.path.log, self.proc_name, pid,cid)
		templ = self.template.format(log_name, self.path.ligandpdbqt(cid), self.path.receptorpdbqt(pid))
		target = '{}.sbatch'.format(id, self.proc_name)
		open(target, 'w').write(templ)

		self.command = 'sbatch ' + target
	
		PairDaemon.prepare(self, pid, cid, templ)

	def resume(self, pid, cid):
		target = '{}.sbatch'.format(id, self.proc_name)
		os.system('rm -f {}'.format(target) )

		PairDaemon.resume(self, pid, cid)
		
