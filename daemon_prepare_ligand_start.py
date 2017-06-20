import sys
from progress import Progress
from daemon_prepare_ligand import PrepareLigand, p, user, root, payload

dir = root + '/' + p._('project.wizard.name')
db = Progress(dir + '/progress.db'))
docking_dir = dir + '/docking'

#PrepareLigand(db, dir, payload).start()
sys.exit(0)
