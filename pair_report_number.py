from parameter import Parameter
from pair import Pair
from path import Path

p = Parameter()
pt = Path(p)

pair = Pair(pt.receptordb, pt.liganddb)

print('total', pair.size(), sep='\t')

pair.close()
