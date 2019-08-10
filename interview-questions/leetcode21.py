class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next 

    def __str__(self):
        str_rep = ""
        cur_node = self
        while(cur_node != None):
            str_rep += str(cur_node.val) + " "
            cur_node = cur_node.next
        return str_rep

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur_node1 = l1
        cur_node2 = l2
        new_list = ListNode(69)
        new_list_head = new_list
        while cur_node1 != None or cur_node2 != None:
            if cur_node1 == None:
                new_list.next = ListNode(cur_node2.val)
                new_list = new_list.next
                cur_node2 = cur_node2.next
            elif cur_node2 == None:
                new_list.next = ListNode(cur_node1.val)
                new_list = new_list.next
                cur_node1 = cur_node1.next
            elif cur_node1.val < cur_node2.val:
                new_list.next = ListNode(cur_node1.val)
                new_list = new_list.next
                cur_node1 = cur_node1.next
            else:
                new_list.next = ListNode(cur_node2.val)
                new_list = new_list.next
                cur_node2 = cur_node2.next
        return new_list_head.next

if __name__ == "__main__":
    l1 = ListNode(1,ListNode(2,ListNode(4)))
    l2 = ListNode(1,ListNode(3,ListNode(4)))
    print(l1)
    print(l2)
    print(Solution().mergeTwoLists(l1,l2))
