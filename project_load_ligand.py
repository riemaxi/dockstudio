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
	print(id)

molecule.commit()

'''
# download ligand structures
molecule.foreachStructure(
	molecule.LIGAND_DOM,
	lambda id, s: print(id, s)
	)
'''

molecule.close()
