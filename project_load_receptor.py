import os
from parameter import Parameter
from receptor import Receptor

p = Parameter()

#locate tree
dir = p._('project.dir')
name = p._('project.wizard.create.name')
project_dir = dir + '/' + name

receptors = '{}/{}'.format(project_dir, p._('project.wizard.load.receptor'))

# import ligands
molecule = Receptor(p._('project.molecule.db'))

# import data
for id in open(receptors):
	id = id.strip('\n')
	molecule.add(id)
	print(id)

molecule.commit()

'''
# download structures
molecule.foreachStructure(
	molecule.RECEPTOR_DOM,
	lambda id, s: print(id, s)
	)
'''

molecule.close()
