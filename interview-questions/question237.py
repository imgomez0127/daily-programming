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
    symmetrical = True
    for i in range(len(tree.links)//2):
        symmetrical &= (all_links[i] == all_links[-i-1])
    return symmetrical
def by_level_approach(root):
    q = queue.Queue()
    q.put(root)
    while(not q.empty()):
        cur_nodes = []
        while(not q.empty()):
            cur_nodes += [q.get()]
        for i in range(len(cur_nodes)//2):
            if cur_nodes[i].val != cur_nodes[-i-1].val:
                return False
        for nodes in cur_nodes:
            for node in nodes.links:
                q.put(node)
    return True
if __name__ == "__main__":
    leaf1 = Node(9)
    leaf2 = Node(3)
    leaf3 = Node(5)
    mid1 =Node(3,links=[leaf1])
    mid2 = Node(3,links=[leaf2])
    root = Node(4,links=[mid1,leaf3,mid2])
    print(f(root))
    print(by_level_approach(root))
