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

def test():
	token1 = "x"
	token2 = "y"
	constant1 = "123"
	token3 = "z"
	constant2 = "string constant"
	notAddedtoken = "h"
	duplicatedToken = "x"

	st = SymbolTable()

	st.addWrapper(token1)
	st.addWrapper(token2)
	st.addWrapper(constant1, -1)	
	st.addWrapper(token3)
	st.addWrapper(constant2, -1)
	
	result1 = st.getWrapper(token1)
	if result1 != -1:
		print("token1 exists in the symbol table and has position ", result1.position)

	result2 = st.getWrapper(token2)
	if result2 != -1:
		print("token2 exists in the symbol table and has position ", result2.position)

	result3 = st.getWrapper(constant1)
	if result3 != -1:
		print("token3 exists in the symbol table and has position ", result3.position)

	result4 = st.getWrapper(token3)
	if result4!= -1:
		print("token4 exists in the symbol table and has position ", result4.position)

	result5 = st.getWrapper(constant2);
	if result5!= -1:
		print("token5 exists in the symbol table and has position ", result5.position)

	nonExistingTokenResult = st.getWrapper(notAddedtoken);
	if nonExistingTokenResult == -1:
		print("token not found")
	
	resultDuplicated = st.getWrapper(duplicatedToken);
	if resultDuplicated != -1:
		print("duplicatedToken exists in the symbol table and has position ", resultDuplicated.position)


if __name__ == "__main__":
	test()