import os
from parameter import Parameter
from receptor import Receptor

p = Parameter()

dir = p._('project.dir') + '/'
project_dir = dir + p._('project.wizard.create.name')
data_dir = project_dir + '/data/'

molecule = Receptor(data_dir + p._('project.wizard.receptor.db'))

columns = p._('project.wizard.receptor_report.columns')
molecule.foreachRecord(
	columns,
	lambda id, fields: print(id, fields, sep = '\t')
	)

molecule.close()
