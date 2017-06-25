#!/bin/bash -l

#SBATCH -t 00:20:00
#SBATCH --qos=high-throughput

# run
prepare_gpf4.py -l /home/ferrer/dockstudio/project/toxim/data/structure/ligand/20006.pdb -r receptor.pdbqt -y -o receptor.gpf
