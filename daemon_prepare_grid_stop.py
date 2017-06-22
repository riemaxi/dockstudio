from signal import SIGTERM
import os
from daemon_prepare_grid import PrepareGrid, pt, process_name

try:
	pid = int(open(pt.pidfile(process_name)).read().strip('\n'))
	os.kill(pid, SIGTERM)
except OSError as e:
	pass

pt.clear(process_name)
