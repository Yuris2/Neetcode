# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        if not head:
            return head
        l = head
        r = head.next
        while r:
            l.next = prev
            prev = l
            l = r
            r = r.next
        l.next = prev
        return l