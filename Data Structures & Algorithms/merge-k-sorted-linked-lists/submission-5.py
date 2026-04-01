# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import collections

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i in range(len(lists)):
            node = lists[i]
            heap.append([node.val,i, node])
        
        heapq.heapify(heap)
        dummyNode = ListNode()
        curr = dummyNode

        while heap:
            val, index, node = heapq.heappop(heap)
            curr.next = node

            curr = curr.next
            node = node.next

            if node:
                heapq.heappush(heap, [node.val, index, node])
        
        return dummyNode.next

        