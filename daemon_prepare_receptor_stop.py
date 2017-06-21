from signal import SIGTERM
import os
from daemon_prepare_receptor import PrepareReceptor, pt

try:
	pid = int(open(pt.pidfile).read().strip('\n'))
	os.kill(pid, SIGTERM)
except OSError as e:
	print(e)

os.system('rm ' + pt.pidfile)
os.system('rm ' + pt.stdout)

