#!/usr/bin/env python3

#https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/submissions

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''
def lca_helper(root, v1, v2):
    if not root:
        return root
    if v1 <= root.info <= v2:
        return root
    if v1 < root.info:
        return lca_helper(root.left, v1, v2)
    if v1 > root.info:
        return lca_helper(root.right, v1, v2)
    return root

def lca(root, v1, v2):
    return lca_helper(root, min(v1,v2), max(v1,v2))
