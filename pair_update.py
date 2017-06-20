import sys
import os
from parameter import Parameter
from pair import Pair
from path import Path

p = Parameter()
pt = Path(p)

pair = Pair(pt.data + p._('project.wizard.pair.db'))
pair.clear()

for tpl in sys.stdin:
	pid, cid = tpl.strip('\n').split('\t')

	filename = pt.pairdir(pid, cid)
	if not os.path.isdir(filename):
		print(pid, cid, filename, sep='\t')

pair.commit()
pair.close()
