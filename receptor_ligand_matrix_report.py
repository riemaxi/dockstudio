from parameter import Parameter
from ligand import Ligand
from receptor import Receptor

def line(id, ligand):
	ids = [str(id)]
	ligand.foreachId(
		lambda id: ids.append(str(id))
	)
	return '\t'.join(ids)

p = Parameter()

ligand = Ligand(p._('project.ligand.db'))
receptor = Receptor(p._('project.receptor.db'))

receptor.foreachId(
	lambda id: print(line(id, ligand))
)

ligand.close()
receptor.close()
