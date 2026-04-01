# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #We are going to use a two pointer approach to first determine the node before
    #the nth node from the end
        dummyNode = ListNode()
        dummyNode.next = head
        
        l, r = dummyNode, head


        #Moving right pointer to be n nodes away
        while n > 0 and r:
            r = r.next
            n -= 1
        
        #Moving right pointer until it hits the end
        while r:
            r = r.next
            l = l.next
        
        #When right if out of bounds, left pointer will be at node before 
        #Desired removed node
        l.next = l.next.next
        return dummyNode.next

        