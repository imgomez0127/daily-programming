"""
    This question was asked by palantir
    perform an inorder traversal without using recursion
"""
from queue import LifoQueue
class Node(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def fun(root):
    if(root == None):
        return []
    stack = LifoQueue()
    lst = []
    stack.put(root)
    root = root.left
    while(not stack.empty() or root != None):
        if(root == None):
            root = stack.get()
            lst.append(root.val)
            root = root.right
        else:
            stack.put(root)
            root = root.left
    return lst
if __name__ == "__main__":
    tree = Node(4,Node(2,Node(1),Node(3)),Node(6,Node(5),Node(7)))
    print(fun(tree))
