import re
import glob
import ntpath

names = glob.glob('project/toxim/stage/*.pdb')

names = '\n'.join([ntpath.basename(path) for path in names])

print(names)
m = re.search('1dIY.pDb',names, re.IGNORECASE)

print('match: ', m.group(0))
