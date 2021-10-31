# Vranciu Adrian - 1 A

# Binary search tree
class Node:
	def __init__(self, data, position):
		self.data = data
		self.position: int = position
		self.right = None
		self.left = None

	def __str__(self) -> str:
		toString = ""
		
		if self.left is not None:
			toString += str(self.left)
		
		toString += "data: {0}, position {1}\n".format(self.data, self.position)

		if self.right is not None:
			toString += str(self.right)

		return toString


class SymbolTable:
	def __init__(self):
		self.root = None # root node
		self.position = -1

	def add(self, data):
		self.position += 1

		self.__addWrapper(data, self.root, self.position)

		return self.position

	def __addWrapper(self, data, current, position):
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
				current.left = self.__addWrapper(data, current.left, position)
			else:
				current.right = self.__addWrapper(data, current.right, position)
			
			return current
	
	def get(self, data):
		return self.__getWrapper(data, self.root)

	def __getWrapper(self, data, current: Node) -> int:
		if current is None:
			return -1

		if current.data == data:
			return current.position
		
		if data < current.data:
			return self.__getWrapper(data, current.left)
		else:
			return self.__getWrapper(data, current.right)

	def __str__(self) -> str:
		if self.root is not None:
			return str(self.root)
		return "Empty"