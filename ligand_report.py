import os
from parameter import Parameter
from ligand import Ligand

p = Parameter()

molecule = Ligand(p._('project.ligand.db'))

columns = p._('project.wizard.ligand_report.columns')
molecule.foreachRecord(
	columns,
	lambda id, fields: print(id, fields, sep = '\t')
	)

molecule.close()
