import re
import glob
import ntpath
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
	return pt.filename('{}.pdb'.format(id), pt.stage, '*.pdb') != None

def copy(id, dir, pt, pids):
	stagefile = pt.filename('{}.pdb'.format(id), pt.stage, '*.pdb')
	os.system('cp {} {}/{}.pdb'.format(stagefile, dir, id.upper()))

	print('!','stage: ', id, sep = '\t')
	
def save(id,s,format, dir, pt, pids):
	if s != None:
		filename = '{}/{}.{}'.format(dir, id, format)
		with open(filename,'w') as file:
			file.write(s)
	else:
		pids.append(id)

	print('!' if s!=None else '?', 'rcsb: ', id,  sep = '\t')

structure_dir = data_dir + 'structure/receptor'
pids = []
molecule.foreachStructure(
	lambda id, s, format: save(id, s, format, structure_dir, pt, pids),
	lambda id: not instage(id, pt),
	lambda id: copy(id, structure_dir, pt, pids)
	)

molecule.rem(pids)

molecule.close()
