"""
	Asked by elgoog
"""
class Node(object):
	def __init__(self,val,left=None,right=None):
		self.val = val
		self.left = left
		self.right = right
	def toString(self,root,level):
		if(root == None):
			return " " * (2*level) + "None"
		curStr = " " * (2*level) + "(" +  str(root.val) + "\n"
		curStr += self.toString(root.left,level+1) + "\n"
		curStr += self.toString(root.right,level+1) + ")"
		return curStr
	def __str__(self):
		return self.toString(self,0)
def isUnival(root,val):
	if(root == None):
		return True
	return root.val == val and isUnival(root.left,val) and isUnival(root.right,val)
def findUnivalTrees(root):
	if(root == None):
		return 0
	return isUnival(root,root.val) + findUnivalTrees(root.left) + findUnivalTrees(root.right)
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(1)
	root.right = Node(0)
	root.right.left= Node(1)
	root.right.left.left = Node(1)
	root.right.left.right = Node(1)
	root.right.right = Node(0)
	print(root)
	print(findUnivalTrees(root))