#!/bin/bash -l

#SBATCH -t 10:00:00
#SBATCH --qos=high-throughput
#SBATCH -o {}

# run
autodock4 -p ligand_receptor.dpf -l scoring.log
