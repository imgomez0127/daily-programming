#!/usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:

    def isSymmetric(self, root):
        q = Queue()
        q.put(root)
        valid = True
        while not q.empty():
            lst = []
            while not q.empty():
                lst.append(q.get())
            for i in range(round(len(lst)/2)):
                if lst[i] and lst[len(lst)-i-1]:
                    if lst[i].val != lst[len(lst)-i-1].val:
                        return False
                else:
                    valid &= not lst[i] and not lst[len(lst)-i-1]
            for node in lst:
                if node:
                    q.put(node.left)
                    q.put(node.right)
        return valid

    def symmetric_helper(self, r1,r2):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        return (r1.val == r2.val
                and self.symmetric_helper(r1.left, r2.right)
                and self.symmetric_helper(r1.right, r2.left))

    def is_symmetric_rec(self, root):
        if not root:
            return True
        return self.symmetric_helper(root.left,root.right)
