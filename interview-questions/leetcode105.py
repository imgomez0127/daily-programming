def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    if(preorder == []):
        return None
    if(len(preorder) == 1):
        return TreeNode(preorder[0])
    root = TreeNode(preorder[0])
    middle = root.index(preorder[0])
    root.left = buildTree(preorder[1:middle+1],inorder[:middle])
    root.right = buildTree(preorder[middle+1:],inorder[middle+1:])
    return root
