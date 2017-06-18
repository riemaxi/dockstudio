import os
from parameter import Parameter
from ligand import Ligand

p = Parameter()

#locate tree
dir = p._('project.dir')
name = p._('project.wizard.create.name')
project_dir = dir + '/' + name

filename = '{}/{}'.format(project_dir,p._('project.wizard.load.ligand'))

#import data
molecule = Ligand(p._('project.molecule.db'))
for id in open(filename):
	id = id.strip('\n')
	molecule.add(id)

molecule.commit()

# download ligand structures
def save(id, s, format, dir):
	filename = '{}/{}.{}'.format(dir,id, format)
	with open(filename,'w+') as file:
		file.write(s)
	print(id)

structure_dir = p._('project.structure.ligand')
molecule.foreachStructure(
	lambda id, s, format: save(id, s, format, structure_dir)
	)

molecule.close()
