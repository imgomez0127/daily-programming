class StackNode:
    def __init__(self,val,next=None,next_max=None):
        self.val = val
        self.next_max = next_max
        self.next = next

class MaxStack:
    def __init__(self):
        self.stack = None
    
    def push(self, val):
        self.stack.append(val) 
    
    def pop(self):
        item = self.stack[-1]
        self.stack.pop()
        return item 

    def max(self):
        return self.max

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
#TODO Gotta figure out how to do this in O(1) time
