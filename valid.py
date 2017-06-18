import sqlite3
from repository import Repository

class Domain:
	repo = Repository()
	def __init__(self, name, domain = 0):
		self.domain = domain
		self.sess = sqlite3.connect(name)
		c = self.sess.cursor()

		c.execute('create table if not exists assignment(domain int, id int,dimension int, value int, primary key(domain,id,dimension))')
		c.execute('create table if not exists value(domain int, id int, data text, primary key(domain,id))')

		self.sess.commit()


	def cashValues(self):
		c = self.sess.cursor()
		self.repo.cash( c.execute('select id, data from value where domain = {0}'.format(self.domain)) )

	def updateAvailableId(self):
		self.repo.update()

	def mapValue(self, data):
		return self.repo.add(data)

	def addValue(self, location, dimension, data, default = '', on_duplicate='replace', commit = False):
		c = self.sess.cursor()
		id = self.mapValue(default if data == None else data)
		query = 'insert or {} into assignment values({},{},{},{})'.format(on_duplicate, self.domain,location,dimension, id)
		c.execute(query)
		if commit:
			self.sess.commit()


	def exists(self, fields):
		c = self.sess.cursor()
		select = "select e.dimension from assignment e join value v on e.value = v.id where e.domain = {0} and  e.dimension={1} and v.data = '{2}'"
		union = '\n union \n'.join([ select.format(self.domain, f[0], str(f[1]).replace("'","''")) for f in fields ])
		query = 'select count(dimension) from ({0})'.format(union)

		try:
			result = c.execute(query).fetchone()

			return (result[0] != None) and (result[0] == len(fields))
		except Exception as e:
			print(e)
			print(query)
			return False


	def idExists(self, id):
		c = self.sess.cursor()
		c.execute('select id from assignment where id = {}'.format(id))
		result = c.fetchone()
		return result != None


	def addEntity(self, id, fields = [], on_duplicate='replace', commit = False):
		exists = self.exists(fields)
		if not exists:
			for field in fields:
				self.addValue(id,field[0],field[1],'', on_duplicate,commit)

		return not exists


	def pushEntity(self, id, fields = [],on_duplicate='replace', commit = False):
		for field in fields:
			self.addValue(id,field[0],field[1],'', on_duplicate, commit)


	def getMaxEntityId(self):
		c = self.sess.cursor()
		c.execute('select max(id) from assignment where domain = {0}'.format(self.domain))
		result = c.fetchone()
		return 0 if result[0] == None else result[0]

	def clear(self):
		c = self.sess.cursor()

		c.execute('delete from assignment where domain = {0}'.format(self.domain))
		c.execute('delete from value where domain = {0}'.format(self.domain))

		self.sess.commit()
		self.repo.clear()

	def saveValueMap(self):
		c = self.sess.cursor()
		self.repo.foreach(
			lambda data,id: c.execute('insert or ignore into value values (?,?,?)',(self.domain, id, data))
		)

	def commit(self):
		self.saveValueMap()
		self.sess.commit()

	def close(self):
		self.sess.close()


	def foreachValue(self, sink, criteria = '1=1'):
		c = self.sess.cursor()
		result = c.execute('select v.* from value v where domain = {0} and {1}'.format(self.domain,criteria))

		for value in result:
			sink(value)

	def foreach(self, sink, criteria = '1=1', idIdx = -1):
		c = self.sess.cursor()
		query = 'select e.id, e.dimension, v.data from assignment e join value v on e.value = v.id where e.domain = {0} and {1} order by e.id, e.dimension, e.value'.format(self.domain, criteria)
		result = c.execute(query)

		id = -1
		entity = {}
		for record in result:
			entity[record[1]] = record[2]

			if id != -1 and id != record[0]:
				entity[idIdx] = id

				keys = sorted([x[0] for x in entity.items()])
				if sink([(k , entity[k]) for k in keys]):
					return
	
			id = record[0]
		
		
		#last one
		entity[idIdx] = id
	
		keys = sorted([x[0] for x in entity.items()])
		sink([(k , entity[k]) for k in keys])


	def xforeach(self, query, sink):
		c = self.sess.cursor()
		result = c.execute(query)
		
		for record in result:
			if sink(record):
				exit
