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
            #if there are not a valid amount of nodes
            if not kthNode:
                break
            
            groupNext = kthNode.next
            #Start reversing the group
            prev, curr = groupNext, groupPrev.next
            #when it hits kth nodes
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            #Fixing the groupPrev
            #1st node (original)
            tmp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = tmp
        
        return dummyNode.next

        
    def findKthNode(self, node,k):
        cur = node
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur
        