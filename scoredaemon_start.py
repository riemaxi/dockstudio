import sys
from pair import Pair
from scoredaemon import ScoreDaemon, p, pt, process_name

user = p._('user')
db = Pair(pt.receptordb, pt.liganddb)

ScoreDaemon(user, db, pt, process_name).start()
sys.exit(0)
