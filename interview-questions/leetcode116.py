"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
""" 
    No extra memory allocation
"""
class Solution:
    def isLeaf(self,root):
            return root.left == None and root.right == None
    def connectRight(self,root,prevRight):
        prevRight.next = root.left
    def connect(self, root: 'Node') -> 'Node':
        if(root == None):
            return None
        if(self.isLeaf(root)):
            return root
        root.left.next = root.right
        if(root.next != None):
            self.connectRight(root.next,root.right)
        self.connect(root.left)
        self.connect(root.right)
        return root
