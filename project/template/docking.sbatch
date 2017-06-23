#!/bin/bash -l

#SBATCH -t 00:20:00
#SBATCH --qos=high-throughput
#SBATCH -o {}

# run
autodock4 -p ligand_receptor.dpf -l scoring.log
