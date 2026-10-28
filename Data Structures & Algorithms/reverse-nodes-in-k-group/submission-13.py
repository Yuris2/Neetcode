# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findKth(self,node,k):
            curr = node
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        groupPrev = dummyNode
        dummyNode.next = head
    
        while True:
            kth = self.findKth(groupPrev, k)

            if not kth:
                break
            
            groupNext = kth.next

            curr = groupPrev.next
            prev = groupNext

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp


        return dummyNode.next

            

         

