import os
from parameter import Parameter

p = Parameter()

# create dir tree
dir = p._('project.dir')
name = p._('project.wizard.create.name')
project_dir = dir + '/' + name

os.system('rm -rf {}'.format(project_dir))

os.system('mkdir {}'.format(project_dir))
os.system('mkdir {}/data'.format(project_dir))
os.system('mkdir {}/data/structure'.format(project_dir))
os.system('mkdir {}/data/structure/receptor'.format(project_dir))
os.system('mkdir {}/data/structure/ligand'.format(project_dir))

os.system('mkdir {}/docking'.format(project_dir))
os.system('mkdir {}/docking/receptor'.format(project_dir))
os.system('mkdir {}/docking/ligand'.format(project_dir))
os.system('mkdir {}/log'.format(project_dir))
os.system('mkdir {}/stage'.format(project_dir))
os.system('mkdir {}/report'.format(project_dir))
