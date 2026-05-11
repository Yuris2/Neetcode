# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyNode = ListNode()
        ptr = dummyNode
        minHeap = []

        for i, lst in enumerate(lists):
            heapq.heappush(minHeap, (lst.val, i, lst))

        while minHeap:
            val, i, node = heapq.heappop(minHeap)

            ptr.next = node
            ptr = node

            node = node.next
            if node:
                heapq.heappush(minHeap, (node.val, i, node))
        
        return dummyNode.next
            
                    
        