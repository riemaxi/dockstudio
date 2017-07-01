from parameter import Parameter
from pair import Pair
from path import Path

p = Parameter()
pt = Path(p)

pair = Pair(pt.receptordb, pt.liganddb)
pair.foreach(
	lambda pid, cid : print(pid, cid, sep = '\t')
)

pair.close()
