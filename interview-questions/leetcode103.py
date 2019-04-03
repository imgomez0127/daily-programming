import queue
"""
    This is a shitty solution
"""
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        q = queue.Queue()
        revQ = queue.Queue()
        useQ = True
        if(root != None):
            q.put(root)
        totalLst = []
        curLst = []
        while(not q.empty() or not revQ.empty()):
            if(useQ):
                curNode = q.get()
                curLst.append(curNode.val)
                if(curNode.left != None):
                    revQ.put(curNode.left)
                if(curNode.right != None):
                    revQ.put(curNode.right)
                if(q.empty()):
                    totalLst.append(curLst)
                    curLst = []
                    useQ = False
            else:
                curNode = revQ.get()
                curLst.append(curNode.val)
                if(curNode.left != None):
                    q.put(curNode.left)
                if(curNode.right != None):
                    q.put(curNode.right)
                if(revQ.empty()):
                    totalLst.append(list(reversed(curLst)))
                    curLst = []
                    useQ = True
        return totalLst
