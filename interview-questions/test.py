class Solution:
    def buildTree(self, inorder, postorder):
        if(len(inorder) == 1):
            return TreeNode(inorder[0])
        indexOfRootforInorder = inorder.indexOf(postorder[-1])
        inorderLeft = inorder[:indexOfRootforInOrder]
        inorderRight = inorder[indexOfRootforInorder+1:] 
        postorderLeft = postorder[:postorder.indexOf(indorderLeft[-1])+1]
        postorderRight = postorder[
        root = TreeNode(postorder[-1])
        root.left = buildTree(inorderLeft,
        root.right = 
        return 
