import sys
import re

for path in sys.stdin:
	content = open(path.strip('\n')).read().split('\n')
	
	pid = path.split('/')[-1].split('.')[0]
	torsion = re.split('\s+',content[0])[1]

	print(pid, torsion, sep = '\t')
	
