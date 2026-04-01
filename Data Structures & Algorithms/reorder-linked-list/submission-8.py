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
        
        secondHalf = slow.next
        slow.next = None

        prev, curr = None, secondHalf

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        secondHalf = prev

        p1, p2 = head, secondHalf

        while p1 and p2:
            t1, t2 = p1.next, p2.next

            p1.next = p2
            p2.next = t1

            p1, p2 = t1, t2
        


        
        