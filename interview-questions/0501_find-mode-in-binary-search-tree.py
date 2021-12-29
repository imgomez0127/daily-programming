# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter

def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts = Counter(inorder(root))
        max_count = max(counts.values())
        return [val for val, count in counts.items() if count == max_count]
