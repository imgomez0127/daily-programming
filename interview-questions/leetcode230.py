class Node(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    if(root == None):
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

def kth_smallest(tree,k):
    return inorder_traversal(tree)[k-1]

if __name__ == "__main__":
    root = Node(3,Node(1,right=Node(2)),Node(4))
    print(kth_smallest(root,1))
