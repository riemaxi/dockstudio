import os
from parameter import Parameter
from receptor import Receptor

p = Parameter()

molecule = Receptor(p._('project.receptor.db'))

columns = p._('project.wizard.receptor_report.columns')
molecule.foreachRecord(
	columns,
	lambda id, fields: print(id, fields, sep = '\t')
	)

molecule.close()
