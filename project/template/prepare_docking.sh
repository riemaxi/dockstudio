#!/bin/bash -l

#SBATCH -t 00:20:00
#SBATCH --qos=high-throughput

# run
prepare_dpf4.py -l ligand.pdbqt -r protein.pdbqt

#rm slurm*.out
touch prepare_docking.done
