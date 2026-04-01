# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1->2->3->4
#p           n
#d->1->2->3->4

#d 3->2->1->4

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        groupPrev = dummyNode

        while True:
            nthNode = self.findKthNode(groupPrev, k)

            if not nthNode:
                break
            
            groupNext = nthNode.next
            prev, curr = groupNext, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            t = groupPrev.next
            groupPrev.next = nthNode
            groupPrev = t
        
        return dummyNode.next

    
    def findKthNode(self, node, k):
        cur = node

        while cur and k > 0:
            cur = cur.next
            k -= 1
        
        return cur

        