# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r = head
        while r and n > 0:
            r = r.next
            n -= 1
        
        dummyNode = ListNode()
        dummyNode.next = head
        l = dummyNode

        while r:
            r = r.next
            l = l.next
        
        l.next = l.next.next
        return dummyNode.next
        