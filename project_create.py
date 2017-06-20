import os
from parameter import Parameter

p = Parameter()

# create dir tree
dir = p._('project.dir')
name = p._('project.wizard.create.name')
project_dir = dir + '/' + name

os.system('rm -r {}'.format(project_dir))

os.system('mkdir {}'.format(project_dir))
os.system('mkdir {}/receptor'.format(project_dir))
os.system('mkdir {}/ligand'.format(project_dir))
os.system('mkdir {}/docking'.format(project_dir))
os.system('mkdir {}/docking/done'.format(project_dir))
os.system('mkdir {}/log'.format(project_dir))
os.system('mkdir {}/template'.format(project_dir))




