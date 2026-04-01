# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummyNode = ListNode()
        dummyNode.next = head

        l = dummyNode
        r = head

        while n > 0 and r:
            r = r.next
            n -= 1
        
        while r:
            r = r.next
            l = l.next
        
        l.next = l.next.next

        return dummyNode.next
        