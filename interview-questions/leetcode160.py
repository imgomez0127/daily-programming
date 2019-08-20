class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cur_nodeA = headA
        cur_nodeB = headB
        seen = set()
        while cur_nodeA != None :
            seen.add(cur_nodeA)
            cur_nodeA = cur_nodeA.next
        while cur_nodeB != None:
            if cur_nodeB in seen:
                return cur_nodeB
            cur_nodeB = cur_nodeB.next
        return None
