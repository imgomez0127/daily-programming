class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.most_frequent_sum = {}

    def treeSum(self,root):
        if root == None:
            return 0
        subtree_sum = (root.val + 
            self.treeSum(root.left) + 
            self.treeSum(root.right)
        )
        self.most_frequent_sum[subtree_sum] = self.most_frequent_sum.get(subtree_sum, 0) + 1
        return subtree_sum

    def findFrequentTreeSum(self, root):
        self.treeSum(root)
        most_frequent_sum = []
        max_sum_frequency = float("-inf")
        for subtree_sum,occurence in self.most_frequent_sum.items():
            if occurence > max_sum_frequency:
                most_frequent_sum = [subtree_sum]
                max_sum_frequency = occurence
            elif occurence == max_sum_frequency:
                most_frequent_sum.append(subtree_sum)
        return most_frequent_sum 
            
if __name__ == "__main__":
    t1 = TreeNode(5,TreeNode(2),TreeNode(-5))    
    t2 = TreeNode(5,TreeNode(2),TreeNode(-3))
    print(Solution().findFrequentTreeSum(t1))
    print(Solution().findFrequentTreeSum(t2))
