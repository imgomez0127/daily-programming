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
    def insertionSortList(self, head):
        if not head:
            return head
        start = Node(float('-inf'), head)
        cur = start.next
        while cur.next:
            # If not sorted do work else skip
            if cur.next.val < cur.val:
                old_next = cur.next
                cur.next = cur.next.next
                tmp = start
                while tmp.next.val < old_next.val:
                    tmp = tmp.next
                old_next.next = tmp.next
                tmp.next = old_next
            else:
                cur = cur.next
        return start.next

if __name__ == "__main__":
    Llist1 = Node(6,next=Node(3))
    Llist = Node(6,Node(5,Node(3,Node(1,Node(8,Node(7,Node(2,Node(4))))))))
    print(Solution().insertionSortList(Llist1))
    print(Solution().insertionSortList(Llist))
