import os
from parameter import Parameter
from ligand import Ligand

p = Parameter()

dir = p._('project.dir') + '/'
project_dir = dir + p._('project.wizard.create.name') + '/'
data_dir = project_dir + 'data/'

molecule = Ligand(data_dir + p._('project.wizard.ligand.db'))

columns = p._('project.wizard.ligand_report.columns')
molecule.foreachRecord(
	columns,
	lambda id, fields: print(id, fields, sep='\t')
	)

molecule.close()
