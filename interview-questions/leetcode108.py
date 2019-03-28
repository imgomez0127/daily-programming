# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from math import ceil
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums == []:
            return None
        middle = ceil(len(nums)/2)
        root = TreeNode(nums[middle])
        root.left = self.sortedArrayToBST(nums[:middle])
        root.right = self.sortedArrayToBST(nums[middle+1:])
        return root
