from sys import argv
class Node(object):
	def __init__(self,key,value):
		self.key = key
		self.value = value
		self.parent = None
		self.left = None
		self.right = None
		self.color = 0
class RBTree(object):
	def __init__(self):
		self.__root = None
	def insert(self,key_value):
		key = key_value[0]
		value = key_value[1]
		if(self.__root == None):
			self.__root = Node(key,value)
			self.__root.color = 1
			return
		parentNode = None
		curNode = self.__root
		while(curNode != None):
			if(curNode.key == key):
				raise ValueError("Attempting to insert key '" + str(key) + "' but it already exists")
			parentNode = curNode
			if(curNode.key > key):
				curNode = curNode.left
			else:
				curNode = curNode.right
		addedNode = Node(key,value)
		if(key<parentNode.key):
			parentNode.left = addedNode
		else:
			parentNode.right = addedNode
		addedNode.parent = parentNode
		self.fixup(addedNode)
	def fixup(self,addedNode):
		while(addedNode.parent != None and addedNode.parent.color == 0):
			if(addedNode.parent == addedNode.parent.parent.left):
				y = addedNode.parent.parent.right
				if(y != None and y.color == 0):
					addedNode.parent.color = 1
					y.color = 1
					addedNode.parent.parent.color = 0
					addedNode = addedNode.parent.parent
				elif(addedNode == addedNode.parent.right):
					addedNode = addedNode.parent
					self.left_rotate(addedNode)
				else:
					addedNode.parent.color = 1
					addedNode.parent.parent.color = 0
					self.right_rotate(addedNode.parent.parent)
			else:
				y = addedNode.parent.parent.left
				if(y != None and y.color == 0):
					addedNode.parent.color = 1
					y.color = 1
					addedNode.parent.parent.color = 0
					addedNode = addedNode.parent.parent
				elif(addedNode.parent.left == addedNode):
					addedNode =  addedNode.parent
					self.right_rotate(addedNode)
				else:
					addedNode.parent.color = 1
					addedNode.parent.parent.color = 0
					self.left_rotate(addedNode.parent.parent)
		self.__root.color = 1
	def left_rotate(self,curNode):
		newParent = curNode.right
		curNode.right = newParent.left
		if(newParent.left != None):
			newParent.left.parent = curNode
		newParent.parent = curNode.parent
		if(curNode.parent == None):
			self.__root = newParent
		elif(curNode == curNode.parent.left):
			curNode.parent.left = newParent
		else:
			curNode.parent.right = newParent
		newParent.left = curNode
		curNode.parent = newParent
	def right_rotate(self,curNode):
		newParent = curNode.left
		curNode.left = newParent.right
		if(newParent.right != None):
			newParent.right.parent = curNode
		newParent.parent = curNode.parent
		if(curNode.parent == None):
			self.__root = newParent
		elif(curNode == curNode.parent.left):
			curNode.parent.left = newParent
		else:
			curNode.parent.right = newParent
		newParent.right = curNode
		curNode.parent = newParent
	def toString1(self,curNode,level):
		if(curNode == None):
			return ((2 * level) * " ") + "None,"
		curString = (2 * level) * " "
		curString += "((" + str(curNode.key)+ ", " + str(curNode.color) + ") ,\n"
		curString += self.toString1(curNode.left,level+1) + "\n"
		curString += self.toString1(curNode.right,level+1)
		curString += ")"
		return curString
	def toString2(self,curNode):
		if(curNode == None):
			return ""
		curString = ""
		curString += self.toString2(curNode.left)
		curString += str(curNode.key) + " " 
		curString += self.toString2(curNode.right)
		return curString
	def __str__(self):
		return self.toString2(self.__root)
if __name__ == "__main__":
	rbtree = RBTree()
	for i in range(1,len(argv)):
		try:
			rbtree.insert((int(argv[i]),1))
		except:
			print("dkbwaubduwiada")

	print(rbtree)