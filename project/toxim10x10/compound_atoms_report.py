import sys
import re

for path in sys.stdin:
	content = open(path.strip('\n')).read().split('\n')
	
	pid = path.split('/')[-1].split('.')[0]
	atoms = ''.join(['1' if line.startswith('HETATM') else '' for line in content])

	print(pid,len(atoms), sep = '\t')
	
