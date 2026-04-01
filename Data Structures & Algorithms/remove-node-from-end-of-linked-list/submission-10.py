# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr1 = head
        
        for _ in range(n):
            ptr1 = ptr1.next

        dummyNode = ListNode()
        dummyNode.next = head
        ptr2 = dummyNode

        while ptr1:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        
        ptr2.next = ptr2.next.next

        return dummyNode.next
        