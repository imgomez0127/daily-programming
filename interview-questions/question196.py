from collections import Counter
class Node(object):
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def compute_subtree_sum(curNode):
    if(curNode == None):
        return 0
    return curNode.data + compute_subtree_sum(curNode.left) + compute_subtree_sum(curNode.right)

def question196(tree):
    counter = Counter()
    def populate_counter(curNode,counter):
        if(curNode == None):
            return
        counter[curNode] += 1
        counter[compute_subtree_sum(curNode)] += 1
        populate_counter(curNode.left,counter)
        populate_counter(curNode.right,counter)
    populate_counter(tree,counter)
    return counter.most_common()[0][0] if len(counter) > 0 else None
if __name__ == "__main__":
    tree = Node(5,Node(2),Node(-5))
    print(question196(tree))
