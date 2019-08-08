class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
    def __str__(self):
        str_representation = ""
        cur_node = self
        while cur_node != None:
            str_representation += str(cur_node.val) + " "
            cur_node = cur_node.next
        return str_representation

class Solution:

    def get(self,node,i):
        cur_node = node
        for _ in range(i):
            cur_node = cur_node.next 
        return cur_node

    def insertionSortList(self, head):
        cur_node = head
        i = 1
        while cur_node != None:
            has_swapped = False
            next_node = head
            swap_val = cur_node.val
            for _ in range(i):
                if not has_swapped and swap_val < next_node.val:
                    temp = next_node.val
                    next_node.val = swap_val
                    swap_val = temp
                    has_swapped = True
                elif has_swapped:
                    temp = next_node.val
                    next_node.val = swap_val
                    swap_val = temp
                next_node = next_node.next
            cur_node = cur_node.next
            i += 1
        return head

if __name__ == "__main__":
    Llist1 = Node(6,next=Node(3))
    Llist = Node(6,Node(5,Node(3,Node(1,Node(8,Node(7,Node(2,Node(4))))))))
    print(Solution().insertionSortList(Llist1))
    print(Solution().insertionSortList(Llist))
