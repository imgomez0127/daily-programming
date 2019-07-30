class Node:
    def __init__(self,left=None,right=None):
        self.left = left
        self.right = right

def height(node):
    if node == None:
        return 0
    return 1+max(height(node.left),height(node.right))

def question(root):
    if root == None:
        return True
    left_subtree_height = height(root.left)
    right_subtree_height = height(root.right)
    return abs(left_subtree_height-right_subtree_height) <= 1 and question(root.left) and question(root.right) 
if __name__ == "__main__":
    root = Node(Node(),Node(Node(Node()))) 
    print(question(root))
