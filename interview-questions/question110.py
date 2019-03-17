"""
    This question was asked by Facebook which is given a binary tree return all
    the paths from the root to the leaves
"""
class Node(object):
    def __init__(self,data,lt=None,rt=None):
        self.data = data
        self.lt = lt
        self.rt = rt
def isLeaf(t):
    return t.lt == None and t.rt == None
def fun(t):
    if(isLeaf(t)):
        return [[t.data]]
    subTreepaths = fun(t.lt)
    subTreepaths.extend(fun(t.rt))
    newPathLst = []
    for path in subTreepaths:
        path =  [t.data] + path
        newPathLst.append(path)
    return newPathLst
if __name__ == "__main__":
    t = Node(1,Node(2),Node(3,Node(4),Node(5)))
    print(fun(t))
