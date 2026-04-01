# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        slow.next = None

        l, r = None, l2
        while r:
            tmp = r.next
            r.next = l
            l = r
            r = tmp
        
        l2 = l
        l1 = head

        while l1 and l2:
            tmp1 = l1.next
            tmp2 = l2.next

            l1.next = l2
            l2.next = tmp1

            l1 = tmp1
            l2 = tmp2


        