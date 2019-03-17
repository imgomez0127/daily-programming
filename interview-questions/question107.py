"""
    Asked by Microsoft print  a Binary Tree by level
"""
class Node(object):
    def __init__(self,val,lt=None,rt=None):
        self.val = val
        self.lt = lt
        self.rt = rt
 
import queue
def fun(t):
    resStr = ""
    q = queue.Queue()
    q.put(t) 
    while(not q.empty()):
        curT = q.get()
        resStr += str(curT.val) + ", "
        if(curT.lt != None):
            q.put(curT.lt)
        if(curT.rt != None): 
            q.put(curT.rt)
    return resStr[:-2]
if __name__ == "__main__":
    t = Node(1,Node(2),Node(3,Node(4),Node(5)))
    print(fun(t))
