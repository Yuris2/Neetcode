# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        groupPrev = dummyNode

        while True:
            kthNode = self.findKthNode(groupPrev, k)

            if not kthNode:
                break
            
            groupNext = kthNode.next
            prev, curr = groupNext, groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp
        
        return dummyNode.next
    
    def findKthNode(self,head,k):
        ptr = head
        for _ in range(k):
            if ptr:
                ptr = ptr.next
        return ptr
        