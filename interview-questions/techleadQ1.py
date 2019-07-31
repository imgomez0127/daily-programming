class Node(object):
    def __init__(self,x,next=None):
        self.val = x
        self.next = next
    def __add__(self,number):
        if(isinstance(number,int)):
            return (self.val + number) 
        return (self.val + number.val) 
    def __str__(self):
        return str(self.val)

class Solution:
    def addTwoNumbers(self,l1,l2,c=0):
        if(l1 == None and l2 == None):
            return None if c == 0 else Node(c)
        if(l2 == None):
            cur_node = Node((l1 + c)%10)
            cur_node.next = self.addTwoNumbers(l1.next,l2,c=(l1+c)//10)
            return cur_node
        if(l1 == None):
            cur_node = Node((l2 + c)%10)
            cur_node.next = self.addTwoNumbers(l1,l2.next,c=(l2+c)//10)
            return cur_node
        cur_node = Node((l1+l2+c)%10)
        cur_node.next = self.addTwoNumbers(l1.next,l2.next,c=(l1+l2+c)//10)
        return cur_node
if __name__ == "__main__":
    l1 = Node(2)
    l1.next = Node(4)
    l1.next.next = Node(3)
    
    l2 = Node(5)
    l2.next = Node(6)
    l2.next.next = Node(4)

    result = Solution().addTwoNumbers(l1, l2)
    print("#",end=" ")
    while result: 
        print(result.val,end = " ")
        result = result.next
    print()
