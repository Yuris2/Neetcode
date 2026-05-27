# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHalf = slow.next
        slow.next = None

        l,r = None, secondHalf

        while r:
            tmp = r.next
            r.next = l
            l = r
            r = tmp
        
        p1, p2 = head,l

        while p1 and p2:
            t1, t2 = p1.next, p2.next

            p1.next = p2
            p2.next = t1

            p1,p2 = t1, t2
        
        
        