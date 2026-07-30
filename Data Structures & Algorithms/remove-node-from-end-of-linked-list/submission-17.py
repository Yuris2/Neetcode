# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #0->1->2->3->4
        dummyNode = ListNode()
        dummyNode.next = head

        curr = head

        while n > 0:
            curr = curr.next
            n -= 1
        
        ptr = dummyNode

        while curr:
            ptr = ptr.next
            curr = curr.next
        
        ptr.next = ptr.next.next

        return dummyNode.next