import sys
from parameter import Parameter

p = Parameter()

title = p._('project.wizard.create.name') + '-heatmap'

template = open('template/heatmap.html').read()

maxscore, columns = next(sys.stdin).strip('\n').split('\t',1)

minscore = float('+inf')
y = 1
data = []
for line in sys.stdin:
	scores = [float(s) for s in line.strip('\n').split('\t')[1:]]
	minscore = min(minscore, min(scores))
	
	data += ['x:{}, y:{}, value:{}, radius: 20'.format(x+1,y,scores[x]) for x in range(len(scores))]

	y += 1

template = template.replace('_DS_TITLE_DS_', title)
template = template.replace('_DS_MIN_DS_', str(minscore))
template = template.replace('_DS_MAX_DS_', str(maxscore))
template = template.replace('_DS_DATA_DS_', '},{'.join(data))

print(template)
