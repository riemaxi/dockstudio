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

def load_number(path):
	content = open(path).read().strip('\n').split('\n')
	map = {}
	for pair in content:
		cid, number = pair.split('\t')
		map[cid] = number
	return map

def getfloat(s):
	try:
		return float(s)
	except:
		return '?'

compounds = next(sys.stdin).strip('\r\n').split('\t')[2:]
compounds = [c.split('_')[2] for c in compounds]

protein = load_protein('report/sop_protein.tsv')
sop = load_sop('report/assay_sop.tsv')
atoms = load_number('report/cid_atoms.tsv')
torsions = load_number('report/cid_torsions.tsv')

for line in sys.stdin:
	assay, category, scores = line.strip('\n').split('\t',2)
	
	scores = scores.split('\t')
	for i in range(len(scores)):
		sopid = sop.get(assay)
		pid = protein.get(sopid)
		cid = compounds[i]
		score = getfloat(scores[i])
		a = atoms.get(cid)
		t = torsions.get(cid)
		print('!' if pid and a else '?',score, pid, cid, a, t, sep = '\t')
