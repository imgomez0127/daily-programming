"""
    Asked by Google
"""
class Node(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def isLeaf(root):
    return root.left == None and root.right == None
def fun(root, targetVal):
    def fun_helper(root,differenceDict,targetVal):
        if(isLeaf(root)):
            if(root.val in differenceDict):
                return (root,differenceDict[root.val])
            return None
        if(root.val in differenceDict):
            return (root,differenceDict[root.val])
        differenceDict[root.val-targetVal] = root
        answer = fun_helper(root.left,differenceDict,targetVal)
        answer2 = fun_helper(root.right,differenceDict,targetVal)
        if(answer != None):
            return answer
        if(answer2 != None):
            return answer2
        return None
    return fun_helper(root,{},targetVal)
if __name__ == "__main__":
    tree = Node(10,Node(5),Node(15,Node(11),Node(15)))
    x = fun(tree,20)
    print(x)
