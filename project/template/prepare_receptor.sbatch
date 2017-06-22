#!/bin/bash -l

#SBATCH -t 00:20:00
#SBATCH --qos=high-throughput
#SBATCH -o {}

#run
obabel -ipdb {} -opdbqt -xr > {}.pdbqt
