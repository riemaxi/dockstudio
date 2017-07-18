import sys
from parameter import Parameter
import math

GAUSS_WIDTH = 20

def gauss(x, u,xscale, yscale = 255):
	x = xscale*x - 10
	return int(yscale * math.exp(-math.pow(x-u,2)/16))

def colorscale(size = 10):
	xscale = GAUSS_WIDTH/size
	result = []
	for i in range(size):
		r = gauss(i,-2,xscale)
		g = gauss(i,2,xscale)
		b = gauss(i,4, xscale)
		result.append('<tr><td width="50" bgcolor="#{:02x}{:02x}{:02x}"></td></tr>'.format(r,g,b))

	return '<table cellspacing="0" cellpadding="0" height="500">\n{}\n</table>'.format('\n'.join(result))

def getcolor(score, mns, mxs, size = 10):
	xscale = GAUSS_WIDTH/size

	if score <= mxs:
		if score >= mns:
			i = size*(score + abs(mns))/(mxs - mns) - 1

			r = gauss(i,-2,xscale)
			g = gauss(i,2,xscale)
			b = gauss(i,4, xscale)

			return '#{:02x}{:02x}{:02x}'.format(r,g,b)
		else:
			return '#fffffe'
	else:
		return '#ffffff'


def heatmap(columns, minscore, maxscore, size):
	data = ['<table cellspacing="0" cellpassing="0" width="500" height="500">',
		'<td/>' + ''.join(['<td>{}</td>'.format(c) for c in columns])]
	for line in sys.stdin:
		line = line.strip('\n').split('\t')
		scores = [float(s) for s in line[1:]]
		data.append('<tr>\n<td>{}</td>'.format(line[0]) + ''.join(['<td bgcolor="{}"></td>'.format(getcolor(score,minscore, maxscore, size)) for score in scores]) + '</tr>')
	
	data.append('</table>')

	return '\n'.join(data)

def title(p):
	return p._('project.wizard.create.name') + '-heatmap'

def scorescale(mns, mxs, size):
	step = (mxs -  mns)/10
	data = ''.join(['<tr><td>{:.2f}</td></tr>'.format(mns + i*step) for i in range(10)])
	return '<table height="500">{}</table>'.format(data)

def html(columns, minscore, maxscore, size, p):
	templ = open('template/heatmap.html').read()
	templ = templ.replace('_DS_TITLE_DS_', title(p))

	templ = templ.replace('_DS_HEATMAP_DS_', heatmap(columns, minscore, maxscore, size))
	templ = templ.replace('_DS_COLOR_SCALE_DS_', colorscale(size))
	templ = templ.replace('_DS_SCORE_SCALE_DS_', scorescale(minscore, maxscore, size))

	return templ

p = Parameter()

minscore = p.f('project.wizard.heatmap.min')
maxscore = p.f('project.wizard.heatmap.max')
size = p.i('project.wizard.heatmap.size')

next(sys.stdin).strip('\n').split('\t') #skip min,max from input

columns = next(sys.stdin).strip('\n').split('\t')

print(html(columns, minscore, maxscore, size, p))
