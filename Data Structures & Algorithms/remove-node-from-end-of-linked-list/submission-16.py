# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = prev = ListNode()
        dummy.next = cur = head

        while cur and n > 0:
            cur = cur.next
            n -= 1
        
        while cur:
            cur = cur.next
            prev = prev.next
        
        prev.next = prev.next.next
        
        return dummy.next


