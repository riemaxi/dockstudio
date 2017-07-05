import sys

def load_docking_score(path):
	map = {}
	for line in open(path):
		assay, compound, score = line.strip('\n').split('\t')
		map['{}_{}'.format(assay,compound)] = score

	return map

def load_atoms_torsions(path):
	map = {}
	for line in open(path):
		compound, atoms, torsions = line.strip('\n').split('\t')
		map[compound] = (atoms, torsions)

	return map

def load_assay_protein(path):
	map = {}
	for line in open(path):
		protein, assay = line.strip('\n').split('\t')
		map[assay] = protein

	return map
		

docking_score = load_docking_score('report/assay__compound__docking_score.tsv')

atoms_torsions = load_atoms_torsions('report/compound_atoms_torsions.tsv')

assay_protein = load_assay_protein('report/protein_assay.tsv')

for line in sys.stdin:
	assay, compound, score = line.strip('\n').split('\t')

	dscore = docking_score.get('{}_{}'.format(assay, compound))
	if dscore != None and dscore != 10000 and score != '0':
		print(assay_protein[assay], compound, score, dscore, atoms_torsions[compound][0], atoms_torsions[compound][1], sep = '\t')
