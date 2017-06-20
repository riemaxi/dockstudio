from parameter import Parameter
from pair import Pair

p = Parameter()

root = p._('root')
dir = root + '/' + p._('project.wizard.name')
pair = Pair(dir + '/pair.db')

pair.foreach(
	lambda pid, cid : print(pid, cid, sep = '\t')
)

pair.close()
