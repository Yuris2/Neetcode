# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# k = 2
#d -> 1 - > 2 - > 3 -> 4
#1     p     c      p

#d  2 ->1-> 3
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
            curr, prev = groupPrev.next, groupNext

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp
        
        return dummyNode.next
            
    def findKthNode(self, node, k):
        curr = node
        while curr and k > 0:
            k -= 1
            curr = curr.next
        return curr
        