# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        prevGroup = dummyNode

        while True:
            kthNode = self.findKthNode(prevGroup, k)

            if not kthNode:
                break
            
            nextGroup = kthNode.next
            prev, curr = nextGroup, prevGroup.next

            while curr != nextGroup:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = prevGroup.next
            prevGroup.next = kthNode
            prevGroup = tmp
        
        return dummyNode.next
        
    def findKthNode(self, head, k):
        curr = head
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
        