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
            nthNode = self.findKthNode(groupPrev,k)
            if not nthNode:
                break
            
            groupNext = nthNode.next
            prev, curr = groupNext, groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            nextGroup = groupPrev.next 
            groupPrev.next = nthNode
            groupPrev = nextGroup
        
        return dummyNode.next
    

    def findKthNode(self, head, k):
        curr = head
        while curr and k > 0:
            curr = curr.next
            k -= 1
        
        return curr

        