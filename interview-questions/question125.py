"""
    Asked by Google
"""
class Node(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def isLeaf(root):
    return root.left == None and root.right == None
def inorderTraversal(root):
    if(isLeaf(root)):
        return [root.val]
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
    
def fun(root, targetVal):
    sortedlst = inorderTraversal(root)
    hashSet = set()
    for element in sortedlst:
        if element in hashSet:
            return (element,targetVal-element)
        else:
            hashSet.add(targetVal-element)         
    return None
if __name__ == "__main__":
    tree = Node(10,Node(5),Node(15,Node(11),Node(15)))
    x = fun(tree,20)
    print(x)
