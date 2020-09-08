#!/usr/bin/env python3
"""
   Name    : leetcode2.py
   Author  : Ian Gomez
   Date    : September 7, 2020
   Description : Add two numbers
   Github  : imgomez0127@github
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1, l2):
        cur = head = ListNode()
        carry = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            new_val = l1_val + l2_val + carry
            carry = new_val//10
            cur.next = ListNode(val=new_val%10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            cur = cur.next
        if carry:
            cur.next = ListNode(val=carry)
        return head.next

if __name__ == "__main__":
    pass
