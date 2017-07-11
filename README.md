# dockstudio
Command line based molecular docking studio. Designed with clusters in mind

the following commands should be executed

module load utilities
module load miniconda/3
module load gcc/6.2.0
module load openbabel

export PATH=$PATH:/home/apps/MGLTools/1.5.6/MGLTools-1.5.6/MGLToolsPckgs/AutoDo$
export PATH=$PATH:/home/ferrer/nodejs/bin

Running the pipeline:

1 - open the parameter.txt file and edit the field "project.wizard.create.name" 
with the name of the project. The following structure will be created under the folder "project":

[name of project]
--data
----structure
------receptor
------ligand
--docking
----ligand
----receptor
--log
--stage

run python project_create.py

2- create two files: ligand.txt and receptor.txt with ids under the folder "stage"
If there are proloaded pdb files, put them also under this folder with the id as name and extension '.pdb'

run in any order
python project_load_receptor.py 
python project_load_ligand.py

two files will be create under data:
ligand.db
receptor.db

pdb files corresponding to ligands and receptors will be placed under the folders
data/structure/ligand and data/structure/receptor respectivelly

3- run
python project daemon_prepare_ligand_start.py
python project daemon_prepare_receptor_start.py

and wait until these processes are finished by checking that the files
log/daemon_prepare_ligand.pid and daemon_prepare_receptor.pid vanish

4- run
python daemon_prepare_grid_start.py
python daemon_create_grid_start.py

and wait for the corresponding pid files vanish like in the previous step

5- run 
python daemon_prepare_docking_start.py and wait until it finishes

6- finally run
python daemon_docking_start.py
python scoredaemon_start.py

the report from scoredaemon (report daemon) is gathered under log with the names

scoring_matrix.txt (matrix form)
scoring_scoring.txt (relational form)
