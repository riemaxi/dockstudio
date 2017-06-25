import re
import os
from parameter import Parameter
from receptor import Receptor
from path import Path

p = Parameter()
pt = Path(p)

#locate tree
dir = p._('project.dir') + '/'
name = p._('project.wizard.create.name')
project_dir = dir + name
data_dir = project_dir + '/data/'

filename = '{}/stage/{}'.format(project_dir, p._('project.wizard.load.receptor'))

# import ligands
molecule = Receptor(data_dir + p._('project.wizard.receptor.db'))
molecule.clear()

# import data
for id in open(filename):
	id = id.strip('\n')
	molecule.add(id)
molecule.commit()

# download structures
def instage(id, pt):
	stagefile = pt.stage + '/{}.pdb'.format(id)
	return os.path.isfile(stagefile)

def move(id, dir, pt):
	stagefile = pt.stage + '/{}.pdb'.format(id)
	os.system('mv {} {}'.format(stagefile, dir))
	print(id)
	
def save(id,s,format, dir, pt):
	filename = '{}/{}.{}'.format(dir, id, format)
	with open(filename,'w') as file:
		file.write(s)

	print(id)

structure_dir = data_dir + 'structure/receptor'
molecule.foreachStructure(
	lambda id, s, format: save(id, s, format, structure_dir, pt),
	lambda id: not instage(id, pt),
	lambda id: move(id, structure_dir, pt)
	)

molecule.close()
