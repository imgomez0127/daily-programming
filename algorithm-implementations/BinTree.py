def stringify(curNode,depth):
		curString = ""
		for i in range(depth):
			curString += "--"
		if curNode == None:
			curString += "None"
			return curString
		curString += str(curNode.data)
		if curNode != None:
			curString += '\n'
			curString += stringify(curNode.left,depth+1)
			curString += '\n'
			curString += stringify(curNode.right,depth+1)
		return curString

class BinTree(object):
	class Node(object):
		def __init__(self,data,left=None,right=None):
			self.data = data
			self.left = left
			self.right = right
		def __str__(self):
			return stringify(self,0)
	def __init__(self, data=None):
		if(data == None):
			root = None
		self.root = self.Node(data)
	def buildBSTHelper(self,lst):
		if len(lst) == 0:
			return None
		center = len(lst)//2
		return self.Node(lst[center],self.buildBST(lst[:center]),self.buildBST(lst[center+1:]))
	def buildBST(self,lst):
		self.root = self.buildBSTHelper(lst)
		return self.root
	def test(self):
		this = self
		return self
	def __str__(self):
		return stringify(self.root,0)
if __name__ == '__main__':
	yeet = BinTree()
	yeet.buildBST([1,2,3,4,5,6,7])
	print(yeet.test())