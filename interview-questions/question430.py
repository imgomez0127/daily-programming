"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def find_end(self, head: 'Node') -> 'Node':
        current = head
        while(current.next != None):
            current = current.next
        return current

    def flatten(self, head: 'Node') -> 'Node':
        if(head == None):
            return None
        current = head
        while(current.next != None or current.child != None):
            if(current.next == None and current.child != None):
                current.next = self.flatten(current.child)
                current.next.prev = current
                current.child = None
                current = current.next
            elif(current.child != None):
                flattened_child = self.flatten(current.child)
                end_of_child = self.find_end(flattened_child)
                current.child = None
                current.next.prev = end_of_child
                end_of_child.next = current.next
                current.next = flattened_child
                current.next.prev = current
                current = end_of_child.next
            else:
                current.child = None
                current = current.next
        return head
