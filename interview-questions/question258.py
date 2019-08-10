from collections import deque
class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def boustrophedon_printing(node):
    deck = deque()
    deck.append(None)
    deck.append(node)
    depth = 0
    entire_list = []
    while len(deck) != 0:
        if depth % 2 == 0:
            cur_node = deck.pop()
            if cur_node != None:
                entire_list.append(cur_node.val)
                if(cur_node.left != None):
                    deck.appendleft(cur_node.left)
                if(cur_node.right != None):
                    deck.appendleft(cur_node.right)
            else:
                if len(deck) != 0:
                    depth += 1
                    deck.append(None)
        else:
            cur_node = deck.popleft()
            if cur_node != None:
                entire_list.append(cur_node.val)
                if(cur_node.right != None):
                    deck.append(cur_node.right)
                if(cur_node.left != None):
                    deck.append(cur_node.left)
            else:
                if len(deck) != 0:
                    depth += 1
                    deck.appendleft(None)
    return entire_list               
if __name__ == "__main__":
    tree = Node(1,Node(2,Node(4),Node(5)),Node(3,Node(6),Node(7))) 
    print(boustrophedon_printing(tree))
