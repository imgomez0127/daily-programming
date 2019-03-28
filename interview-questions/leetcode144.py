class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if(root == None):
            return []
        leftTraversal = self.preorderTraversal(root.left)
        rightTraversal = self.preorderTraversal(root.right)
        return [root.val] + leftTraversal + rightTraversal
