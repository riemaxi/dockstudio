from signal import SIGTERM
import os
from scoredaemon import  pt, process_name

try:
	pid = int(open(pt.pidfile(process_name)).read().strip('\n'))
	os.kill(pid, SIGTERM)
except OSError as e:
	pass

pt.clear(process_name)
os.system('rm -f {}*'.format(process_name))
