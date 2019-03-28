class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if(head == None):
            return None
        countingNode = head
        count = 0
        while(countingNode != None):
            count += 1
            countingNode= countingNode.next
        middle = count//2
        curNode = head
        for _ in range(middle):
            curNode = curNode.next
        root = TreeNode(curNode.val)
        leftLst = head
        root.left = 
             
