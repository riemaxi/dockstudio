import os
from parameter import Parameter
from ligand import Ligand
from receptor import Receptor
from path import Path

def print_pairs(pid, ligand):
	ligand.foreachId(
		lambda cid: print(pid, cid, sep='\t')
	)

p = Parameter()
pt = Path(p)

ligand = Ligand( pt.data + p._('project.wizard.ligand.db'))
receptor = Receptor(pt.data + p._('project.wizard.receptor.db'))

receptor.foreachId(
	lambda id: print_pairs(id, ligand)
)

ligand.close()
receptor.close()
