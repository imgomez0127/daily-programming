class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def serialize(root):
	if(root == None):
		return "None"
	curStr = str(root.val) + "\n"
	curStr += serialize(root.left) + "\n"
	curStr += serialize(root.right)
	return curStr
def deserialize(serializedStr):
	def deserialize_helper(splitArr):
		if(splitArr[0] == None):
			return None
		root = Node(splitArr[0])
		root.left = Node()
	return deserialize_helper(serializedStr.split("\n"))
if __name__ == '__main__':
	node = Node('root', Node('left', Node('left.left')), Node('right'))
	print(serialize(node))
