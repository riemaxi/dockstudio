import sys
import string

class Parameter:
        def __init__(self, prefix = '', path = 'parameter.txt', sep = ':'):
                self.data = {}
                for line in open(path):
                        line = line.strip()
                        if len(line)>0 and (not line.startswith('#')) and line.startswith(prefix):
                                line = line.split(sep)
                                key = line[0].strip().replace(prefix,'')
                                value = line[1].strip() if len(line)>1 else 0
                                self.data[key] = value
                
        def _(self,key, default = 0):
                try:
                    	return self.data[key]
                except:
                       	return default

        def i(self, key, default = 0):
                return int(self._(key, default))

        def f(self, key, default = 0):
                return float(self._(key, default))
