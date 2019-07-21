"""
    This question was asked by Amazon 
    Given a k-tree figure out if it is symmetrical
"""
import queue
class Node(object):
    def __init__(self,val,links=[]):
        self.val = val
        self.links = links
    
def preorder_traversal(tree):
    if tree.links == []:
        return [tree.val]
    child_trees = []
    for node in tree.links:
        child_trees += preorder_traversal(node)
    return [tree.val] + child_trees 
    
def f(tree): 
    all_links = []
    for cur_node in tree.links:
        all_links.append(preorder_traversal(cur_node))
    print(all_links)
    symmetrical = True
    for i in range(len(tree.links)//2):
        symmetrical &= (all_links[i] == all_links[-1])
    return symmetrical

if __name__ == "__main__":
    leaf1 = Node(9)
    leaf2 = Node(9)
    leaf3 = Node(5)
    mid1 =Node(3,links=[leaf1])
    mid2 = Node(3,links=[leaf2])
    root = Node(4,links=[mid1,leaf3,mid2])
    print(f(root))
