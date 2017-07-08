import sys

def load_protein(path):
	content = open(path).read().strip('\n').split('\n')
	protein = {}
	for pair in content:
		sop, pid = pair.split('\t')
		protein[sop] = pid
	return protein

def load_sop(path):
	content = open(path).read().strip('\n').split('\n')
	sop = {}
	for pair in content:
		assay, sopid = pair.split('\t')
		sop[assay] = sopid
	return sop

compounds = next(sys.stdin).strip('\r\n').split('\t')[2:]
compounds = [c.split('_')[2] for c in compounds]

protein = load_protein('report/sop_protein.tsv')
sop = load_sop('report/assay_sop.tsv')

for line in sys.stdin:
	assay, category, scores = line.strip('\n').split('\t',2)
	
	scores = scores.split('\t')
	for i in range(len(scores)):
		sopid = sop.get(assay)
		pid = protein.get(sopid)
		if sopid and pid:
			print(scores[i], pid, compounds[i], sep = '\t')
