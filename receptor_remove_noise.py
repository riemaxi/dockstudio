from parameter import Parameter
from path import Path
from receptor import Receptor
import re

def ok(line):
	field = re.split('\s+', line)
	if field[0] == 'ANISOU':
		return False

	if field[0] in ['ATOM','HETATM']:
		return field[2].upper() not in ['NA']

	return True

def remove_noise(id, path, incl):
	if id in incl:
		content = open(path).read().strip('\n').split('\n')
		newcontent = [s for s in content if ok(s)]

		if len(content) != len(newcontent):
			open(path,'w').write('\n'.join(newcontent))
			print(id)
	
p = Parameter()
pt = Path(p)

molecule = Receptor(pt.receptordb)
incl = p._('project.wizard.receptor_remove_noise.include').split(',')

molecule.foreachId(
	lambda id: remove_noise(id, pt.receptor(id), incl)
)

