# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        l,r = dummyNode, head

        while n > 0:
            r = r.next
            n -= 1
        
        while r:
            l = l.next
            r = r.next
        
        # l points at the nth node in the list
        l.next = l.next.next

        return dummyNode.next

        




        