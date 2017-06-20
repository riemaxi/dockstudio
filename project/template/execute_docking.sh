#!/bin/bash -l

#SBATCH -t 05:00:00
#SBATCH --qos=high-throughput

# run
autodock4 -p ligand_protein.dpf -l scoring.log

#rm slurm*.out
touch execute_docking.done
