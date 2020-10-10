class Node:
    def __init__(self,x,left=None,right=None):
        self.x = x
        self.left = left
        self.right = right

def is_leaf(node):
    return not node.left and not node.right

def inorder(T):
    if T is None:
        return
    if is_leaf(T):
        yield T.x
    else:
        yield from inorder(T.left)
        yield T.x
        yield from inorder(T.right)

def inorder_2(T):
    if T is None:
        return
    if is_leaf(T):
        yield T.x
    else:
        for x in inorder(T.left):
            yield x
        yield T.x
        for x in inorder(T.right):
            yield x

def validate_bst(T):
    inorder_traversal = inorder(T)
    is_valid = True
    previous_node = next(inorder_traversal)
    for current_node in inorder_traversal:
        is_valid &= current_node > previous_node
        previous_node = current_node
    return is_valid

def validate_bst_2(T):
    inorder_traversal = inorder_2(T)
    is_valid = True
    previous_node = next(inorder_traversal)
    for current_node in inorder_traversal:
        is_valid &= current_node > previous_node
        previous_node = current_node
    return is_valid

def validate_bst_helper(T,min_val,max_val):
    if not T:
        return True
    left_rec = validate_bst_helper(T.left,T.left.x,max_val) if T.left else True
    right_rec = validate_bst_helper(T.right,min_val,T.right.x) if T.right else True
    return (min_val <= T.x <= max_val) and left_rec and right_rec

def validate_bst3(T):
    return validate_bst_helper(T,T.x,T.x)

if __name__ == "__main__":
    T1 = Node(2,Node(1,Node(0)),Node(4,Node(3),Node(5)))
    T2 = Node(2,Node(3),Node(1))
    T3 = Node(2,Node(1))
    print(validate_bst(T1))
    print(validate_bst(T2))
    print(validate_bst(T3))
    print(validate_bst_2(T1))
    print(validate_bst_2(T2))
    print(validate_bst_2(T3))
    print(validate_bst3(T1))
    print(validate_bst3(T2))
    print(validate_bst3(T3))
    print(list(inorder(T1)))
