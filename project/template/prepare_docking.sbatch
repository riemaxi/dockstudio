#!/bin/bash -l

#SBATCH -t 00:20:00
#SBATCH --qos=high-throughput
#SBATCH -o {}

# run
prepare_dpf4.py -l ligand.pdbqt -r receptor.pdbqt
