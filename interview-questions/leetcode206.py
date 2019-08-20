# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        cur_node = head
        next_node = head.next
        prev_node = None
        while next_node != None:
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
            next_node = next_node.next
        cur_node.next = prev_node
        return cur_node
