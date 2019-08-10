# Definition for a binary tree node.
class Node(object):
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def is_leaf(self,root):
        return root.left == None and root.right == None
    def max_sum_from_node(self,root):
        if root == None:
            return 0
        left_subtree_val = self.max_sum_from_node(root.left)
        right_subtree_val = self.max_sum_from_node(root.right)
        root_with_left_subtree = left_subtree_val + root.val
        root_with_right_subtree = right_subtree_val + root.val
        return max(root.val,root_with_left_subtree,root_with_right_subtree,root_with_right_subtree)
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return -2147483648
        if self.is_leaf(root):
            return root.val
        left_max_path = self.maxPathSum(root.left)
        right_max_path = self.maxPathSum(root.right)
        return max(root.val,root.val+left_max_path+right_max_path,left_max_path,right_max_path)

if __name__ == "__main__":
    tree1 = Node(1,Node(2),Node(3))
    tree2 = Node(-10,left=Node(9),right=Node(20,left=Node(15),right=Node(7))) 
    print(Solution().maxPathSum(tree1)) 
    print(Solution().maxPathSum(tree2))
