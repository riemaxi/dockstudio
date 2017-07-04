import sys

def load_docking_score(path):
	map = {}
	for line in open(path):
		assay, compound, score = line.strip('\n').split('\t')
		map['{}_{}'.format(assay,compound)] = score

	return map
		

docking_score = load_docking_score('report/assay__compound__docking_score.tsv')

for line in sys.stdin:
	assay, compound, score = line.strip('\n').split('\t')

	dscore = docking_score.get('{}_{}'.format(assay, compound))
	if dscore != None:
		print(assay, compound, score, dscore, sep = '\t')
