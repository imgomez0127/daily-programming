class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if(root == None):
            return []
        leftTraversal = self.inorderTraversal(root.left)
        rightTraversal = self.inorderTraversal(root.right)
        return  leftTraversal + [root.val]  + rightTraversal
