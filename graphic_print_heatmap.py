import math
import sys

def gaussian(x, a, b, c, d=0):
	return a * math.exp(-(x - b)**2 / (2 * c**2)) + d

def create_gradient(limit):
	gradient = []
	for x in range(limit):
		r = int(gaussian(x, 158.8242, 201, 87.0739) + gaussian(x, 158.8242, 402, 87.0739))
		g = int(gaussian(x, 129.9851, 157.7571, 108.0298) + gaussian(x, 200.6831, 399.4535, 143.6828))
		b = int(gaussian(x, 231.3135, 206.4774, 201.5447) + gaussian(x, 17.1017, 395.8819, 39.3148))

		gradient.append( (r,g,b) )
	return gradient

def color(score, gradient):
	index = int(score) - 1
	rgb = gradient[index]
	#print(rgb[0], rgb[1],rgb[2])
	#return '\x1b[{};{};{}m \x1b[0m'.format( rgb[0] , rgb[1], rgb[2] )
	return '\x1b[{};{};{}m \x1b[0m'.format( 30, 40, 50 )

print( next( sys.stdin).strip('\n') )

gradient = create_gradient(200)

for line in sys.stdin:
	label, scores = line.strip('\n').split('\t',1)
	print(label, end='\t')
	scores = '\t'.join( [ color(float(score) * .001, gradient) for score in scores.split('\t') ] )
	print( scores )
