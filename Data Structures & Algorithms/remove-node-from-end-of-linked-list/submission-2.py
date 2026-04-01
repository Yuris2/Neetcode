# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head

        l = dummyNode
        r = head

        #Moving right pointer n nodes away
        while n > 0 and r:
            r = r.next
            n -= 1
        
        #Getting the node before the noe we want to remove
        while r:
            r = r.next
            l = l.next
        #Skipping over the node we want to remove
        l.next = l.next.next

        return dummyNode.next
        