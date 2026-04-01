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

        minHeap = []

        for k in range(len(lists)):
            node = lists[k]
            heapq.heappush(minHeap, [node.val, k, node])
        
        while minHeap:
            val, k, node = heapq.heappop(minHeap)
            curr.next = node

            curr = curr.next
            node = node.next

            if node:
                heapq.heappush(minHeap,[node.val, k, node])
        
        return dummyNode.next


        