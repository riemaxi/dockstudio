from valid import Domain

class Pair(Domain):
	def __init__(self, name):
		Domain.__init__(self,name)

	def add(self, pid, cid):
		self.pushEntity(pid, [(cid, '{}_{}'.format(pid,cid))])


	def foreachPair(self, pid, cids, sink):
		for cid in cids:
			if sink(pid, cid):
				return True

	def foreach(self, sink, criteria = ''):
		Domain.foreach(
			self,
			lambda data: self.foreachPair( data[0][1],data[1:], sink)
		)

