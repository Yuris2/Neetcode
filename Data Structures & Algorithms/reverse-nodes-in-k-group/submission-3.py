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
            kthNode = self.getKthNode(groupPrev, k)
            if not kthNode:
                break
            
            groupNext = kthNode.next
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                temp = curr.next 
                curr.next = prev
                prev = curr
                curr = temp
            
            #Fixing groupPrev
            temp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = temp

        return dummyNode.next



    def getKthNode(self, node, k):
        curr = node
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
        