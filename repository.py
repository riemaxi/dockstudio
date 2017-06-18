class Repository:
	FIRST_ID = 0

	value = {}
	availableId = FIRST_ID

	def update(self):
		values = sorted(self.value.values())
		id = self.FIRST_ID - 1
		for v in values:
			if v - id > 1:
				id = min(v,id)
				break
			id = v
		self.availableId = id + 1

	def cash(self, map):
		for key, val in map:
			self.value[key] = val
		self.update()

	def add(self, data):
		id = self.value.get(data)
		if id == None:
			self.value[data] = self.availableId
			id = self.availableId
		self.update()

		return id

	def clear(self):
		self.value = {}
		self.availableId = self.FIRST_ID

	def foreach(self, sink):
		for data,id in self.value.items():
			sink(data, id)
