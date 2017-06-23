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

class Matrix(PairDaemon):
	def __init__(self):
		PairDaemon.__init__(self,
					user,
					db,
					pt,
					payload,
					process_name)


	def score(self, pid, cid):
		score_file = pt.pairdir(pid,cid) + '/scoring.log'

		try:
			with open(score_file) as file:
				data = file.read().split('\n')[::-1]
				score_line = [s for s in data if 'Estimated Free Energy of Binding' in s]
				score =  score_line[0].split('=',1)[1].split()[0]
			return score
		except:
                return '-'


	def process_pair(self, pid, cid):
		pass		
		
