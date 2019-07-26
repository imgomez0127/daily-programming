class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
    def to_str(self,root):
        if(root == None):
            return "None"
        return "(" + str(root.val) + ", " + self.to_str(root.left) + ", " + self.to_str(root.right) + ")"
   
    def __str__(self):
        return self.to_str(self) 

def find_right_subtree(lst):
    for i in range(len(lst)):
        if lst[i] > lst[0]:
            return i
    return 1 
def bstFromPreorder(preorder):
    if(preorder == []):
        return None
    if(len(preorder) == 1):
        return TreeNode(preorder[0])
    root = TreeNode(preorder[0])
    right_sub_tree_start = find_right_subtree(preorder)
    left_sub_tree = [] if preorder[1] > preorder[0] else preorder[1:right_sub_tree_start]
    right_sub_tree = preorder[right_sub_tree_start:]
    root.left = bstFromPreorder(left_sub_tree)
    root.right = bstFromPreorder(right_sub_tree)
    return root

if __name__ == "__main__":
    preorder_tree = [8,5,1,7,10,12]
    tree = bstFromPreorder(preorder_tree)
    print(tree)
