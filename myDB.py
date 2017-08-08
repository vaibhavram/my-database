class Database:
	def __init__(self, parent=None):
		self.values = {}
		self.parent = parent
		self.child = None

	def set(self, var, val):
		self.values[var] = val

	def get(self, var):
		try:
			return self.values[var]
		except KeyError:
			return "NULL"

	def unset(self, var):
		if var in self.values.keys():
			del self.values[var]

	def numequalto(self, val):
		return self.values.values().count(val)

	def begin(self):
		new = Database(parent = self)
		self.child = new
		new.values = dict(self.values)
		return new

	def rollback(self):
		if self.parent:
			new = self.parent
			new.child = None
			return new
		else:
			print('NO TRANSACTION')
			return self

	def commit(self):
		if self.parent is None and self.child is None:
			print('NO TRANSACTION')
		else:
			self.parent = None
			self.child = None

def main():
	current = Database()
	while True:
		command = raw_input('<db> ').split(' ')
		method = command[0].upper()
		if method == 'END':
			quit()
		elif method == 'COMMIT':
			current.commit()
		elif method == 'ROLLBACK':
			current = current.rollback()
		elif method == 'BEGIN':
			current = current.begin()
		elif method == 'SET':
			current.set(command[1], int(command[2]))
		elif method == 'GET':
			print(current.get(command[1]))
		elif method == 'UNSET':
			current.unset(command[1])
		elif method == 'NUMEQUALTO':
			print(current.numequalto(int(command[1])))

main()












