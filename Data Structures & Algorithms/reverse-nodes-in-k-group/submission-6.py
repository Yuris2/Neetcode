# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
#      S

#   dummy-> 2-> 1 -> 3 -> 4-> 5
#          k   p.n  nxt
#               tmp

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        groupPrev = dummyNode

        while True:
        #Find the kth node
            kthNode = self.findKthNode(groupPrev, k)

            if not kthNode:
                break
            #track the next group to reverse
            nextGroup = kthNode.next
            prev, curr = nextGroup, groupPrev.next
            #Reverse the current group
            while curr != nextGroup:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # dummy 2->1->3
            tmp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = tmp
            # dummy -> 1 
            # groupPrev = 1
        return dummyNode.next     
        

        #Fix the pointers

    def findKthNode(self, head, k):
        curr = head
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
        