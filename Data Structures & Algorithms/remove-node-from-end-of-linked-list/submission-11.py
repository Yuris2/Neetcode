# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1->2->3 n =2
# d->1->2->3
# p1    p2
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #We want to find the node we want to remove
        #To find the node we want to remove, space two pointers n away

        dummyNode = ListNode()
        dummyNode.next = head

        ptr1 = dummyNode
        ptr2 = head

        while ptr2 and n > 0:
            ptr2 = ptr2.next
            n -= 1
        
        while ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        ptr1.next = ptr1.next.next

        return dummyNode.next        
        

        