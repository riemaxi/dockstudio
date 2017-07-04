import sys

compounds = next(sys.stdin).strip('\r\n').split('\t')[2:]
compounds = [c.split('_')[2] for c in compounds]

for line in sys.stdin:
	assay, category, scores = line.strip('\n').split('\t',2)
	
	scores = scores.split('\t')
	for i in range(len(scores)):
		print(assay, compounds[i], scores[i], sep = '\t')
