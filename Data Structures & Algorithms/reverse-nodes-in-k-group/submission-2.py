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
            nodeK = self.kthNode(groupPrev, k)
            if not nodeK:
                break
            
            groupNext = nodeK.next
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            #Fixing groupPrev
            tmp = groupPrev.next
            groupPrev.next = nodeK
            groupPrev = tmp
            
        return dummyNode.next
    
    def kthNode(self, node, k):
        cur = node
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur
        