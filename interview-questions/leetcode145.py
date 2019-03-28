class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if(root == None):
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
