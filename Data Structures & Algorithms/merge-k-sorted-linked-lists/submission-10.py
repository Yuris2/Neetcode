# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import collections
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyNode = ListNode()
        curr = dummyNode

        heap = []
        for i,node in enumerate(lists):
            heapq.heappush(heap, [node.val, i, node])
        
        while heap:
            val, index, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            node = node.next
            if node:
                heapq.heappush(heap, [node.val, index, node])
        
        return dummyNode.next

        