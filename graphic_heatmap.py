import sys
from parameter import Parameter
import math

def gauss(x, u,xscale, yscale = 255):
	x = xscale*x - 10
	return int(yscale * math.exp(-math.pow(x-u,2)/16))

def colorscale(mns, mxs, size = 10):
	xscale = 20/size
	result = []
	for i in range(size):
		r = gauss(i,-2,xscale)
		g = gauss(i,2,xscale)
		b = gauss(i,4, xscale)
		result.append('<tr><td width="50" bgcolor="#{:02x}{:02x}{:02x}"></td></tr>'.format(r,g,b))

	return '<table cellspacing="0" cellpadding="0" height="300">\n{}\n</table>'.format('\n'.join(result))

def heatmap():
	data = []
	print('<table cellspacing="0" cellpassing="0" height="500" width="500">')
	for line in sys.stdin:
		scores = [float(s) for s in line.strip('\n').split('\t')[1:]]
		print('<tr>\n' + ''.join(['<td bgcolor="{}"></td>'.format(getcolor(scores[i],minscore, maxscore, size)) for i in range(len(scores))]) + '</tr>')
	
	print('</table>')


def getcolor(score, mns, mxs, size = 10):
	xscale = 20/size
	i = 20*(score + abs(mns))/(mxs - mns)

	if i<20:
		r = gauss(i,-4,xscale)
		g = gauss(i,2,xscale)
		b = gauss(i,4, xscale)

		return '#{:02x}{:02x}{:02x}'.format(r,g,b)
	else:
		return '#{:02x}{:02x}{:02x}'.format(255,255,255)

p = Parameter()

title = p._('project.wizard.create.name') + '-heatmap'

template = open('template/heatmap.html').read()

minscore, maxscore = next(sys.stdin).strip('\n').split('\t')
minscore = float(minscore)
maxscore = 0.0

columns = next(sys.stdin).strip('\n').split('\t')

size = int(maxscore - minscore)

heatmap()
#print(colorscale(minscore,maxscore, size))

'''
template = template.replace('_DS_TITLE_DS_', title)
template = template.replace('_DS_MIN_DS_', str(minscore))
template = template.replace('_DS_MAX_DS_', str(maxscore))
template = template.replace('_DS_DATA_DS_', '},{'.join(data))

print(template)
'''
