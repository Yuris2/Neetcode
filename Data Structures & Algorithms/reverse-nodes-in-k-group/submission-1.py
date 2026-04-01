# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #DummyNode
        #Helper function that finds the node k nodes away (assigning the next group)
        #Reverse the nodes (edge case that)
        #Fix the node that points to the prevGroup
        dummyNode = ListNode()
        dummyNode.next = head

        groupPrev = dummyNode
        while True:
            kthNode = self.findKthNode(groupPrev, k)
            if not kthNode:
                break
            
            groupNext = kthNode.next
            #Reversing Linked List
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            #start of reversed list before reversing | groupPrev
            tmp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = tmp
        
        return dummyNode.next


    def findKthNode(self, node, k):
        cur = node
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur