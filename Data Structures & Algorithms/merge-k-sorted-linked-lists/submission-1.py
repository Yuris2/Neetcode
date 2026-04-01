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

        heap = []
        heapq.heapify(heap)

        for i in range(len(lists)):
            node = lists[i]
            heapq.heappush(heap, [node.val, i, node])
        
        while heap:
            val, i, node = heapq.heappop(heap)
            ptr.next = node
            ptr = node
            node = node.next
            if node:
                heapq.heappush(heap, [node.val, i, node])
        
        return dummyNode.next
        