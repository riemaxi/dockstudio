#!/bin/bash -l

#SBATCH -t 00:20:00
#SBATCH --qos=high-throughput
#SBATCH -o {}

# run
prepare_gpf4.py -l {} -r receptor.pdbqt -y -o receptor.gpf
