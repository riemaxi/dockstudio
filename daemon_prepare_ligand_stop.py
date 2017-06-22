from signal import SIGTERM
import os
from daemon_prepare_ligand import PrepareLigand, pt, process_name

try:
	pid = int(open(pt.pidfile(process_name)).read().strip('\n'))
	os.kill(pid, SIGTERM)
except OSError as e:
	pass

os.system('rm -f ' + pt.pidfile(process_name))
os.system('rm -f ' + pt.stdout(process_name))
os.system('rm -f ' + pt.stderr(process_name))
os.system('rm -f ' + pt.squeue_stats(process_name))
os.system('rm -f {}/{}_*.out'.format(pt.log, process_name))

