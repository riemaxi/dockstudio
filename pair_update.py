import sys
import os
from parameter import Parameter
from pair import Pair
from path import Path

p = Parameter()
pt = Path(p)

pair = Pair(pt.pairdb)
pair.clear()

for tpl in sys.stdin:
	pid, cid = tpl.strip('\n').split('\t')

	dirname = pt.pairdir(pid, cid)
	if not os.path.isdir(dirname):
		pair.add(cid, pid)
		print(pid, cid, dirname, sep='\t')

pair.commit()
pair.close()
