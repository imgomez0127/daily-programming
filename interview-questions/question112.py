class Node(object):
    def __init__(self,data,left=None,right=None,parent=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        if(self.parent != None):
            self.level = self.parent.level + 1
        else:
            self.level = 0 
    
def LCA(nodeA,nodeB):
    if(nodeA == nodeB):
        return nodeA
    if(nodeA.level > nodeB.level):
        return LCA(nodeA.parent,nodeB)
    if(nodeB.level > nodeA.level):
        return LCA(nodeA,nodeB.parent)
    return LCA(nodeA.parent,nodeB.parent)
