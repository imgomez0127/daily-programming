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
        cur = head
        prev_nodes = [cur]
        while cur := cur.next:
            tmp = cur.val
            prev_nodes.append(cur)
            for i in reversed(range(len(prev_nodes))):
                if i == 0:
                    prev_nodes[i].val = tmp
                elif prev_nodes[i-1].val > tmp:
                    prev_nodes[i].val = prev_nodes[i-1].val
                else:
                    prev_nodes[i].val = tmp
                    break
        return prev_nodes[0]

if __name__ == "__main__":
    Llist1 = Node(6,next=Node(3))
    Llist = Node(6,Node(5,Node(3,Node(1,Node(8,Node(7,Node(2,Node(4))))))))
    print(Solution().insertionSortList(Llist1))
    print(Solution().insertionSortList(Llist))
