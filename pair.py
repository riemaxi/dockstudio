from valid import Domain

class Pair(Domain):
	def __init__(self, name):
		Domain.__init__(self,name)

	def add(self, cid, pid):
		self.pushEntity(cid, [(pid, '{}_{}'.format(cid,pid))])


	def foreachPair(self, cid, pids, sink):
		for pid in pids:
			if sink(pid, cid):
				return True

	def foreach(self, sink, criteria = ''):
		Domain.foreach(
			self,
			lambda data: self.foreachPair( data[0][1],data[1:], sink)
		)

