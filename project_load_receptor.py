import os
from parameter import Parameter
from receptor import Receptor

p = Parameter()

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
def save(id,s,format, dir):
	filename = '{}/{}.{}'.format(dir, id, format)
	with open(filename,'w') as file:
		file.write(s)
	print(id)

structure_dir = data_dir + 'structure/receptor'
molecule.foreachStructure(
	lambda id, s, format: save(id, s, format, structure_dir)
	)

molecule.close()
