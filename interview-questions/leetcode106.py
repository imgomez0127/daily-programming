# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#inorder = [9,3,15,20,7]
#postorder = [9,15,7,20,3]
"""
    3
   / \
  9  20
    /  \
   15   7
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if(inorder == []):
            return None
        if(len(inorder) == 1):
            return TreeNode(inorder[0])
        root = TreeNode(postorder[-1])
        rootIndex = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:rootIndex],postorder[:rootIndex])
        root.right = self.buildTree(inorder[rootIndex+1:],postorder[rootIndex:-1])
        return root
