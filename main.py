# Vranciu Adrian - 1 A

# Binary search tree
class Node:
	def __init__(self, data, position):
		self.data = data
		self.position = position
		self.right = None
		self.left = None


class SymbolTable:
	def __init__(self):
		self.root = None # root node
		self.position = -1

	def addWrapper(self, data, position = None):
		pos = position

		if position is None:
			pos = self.position + 1;
			self.position += 1

		self.add(data, self.root, pos)

	def add(self, data, current, position):
		if self.root == None:
			self.root = Node(data, position)
			current = self.root
			return self.root
		else:
			if current == None:
				return Node(data, position)

			if data == current.data:
				return current

			if data < current.data:
				current.left = self.add(data, current.left, position)
			else:
				current.right = self.add(data, current.right, position)
			
			return current
	
	def getWrapper(self, data):
		return self.get(data, self.root)

	def get(self, data, current):
		if current is None:
			return -1

		if current.data == data:
			return current
		
		if data < current.data:
			return self.get(data, current.left)
		else:
			return self.get(data, current.right)
