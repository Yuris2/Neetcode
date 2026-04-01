# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        #O(k)
        heapq.heapify(heap)

        for i in range(len(lists)):
            node = lists[i]
            #O(log(k))
            heapq.heappush(heap,[node.val, i, node])

        dummyNode = ListNode()
        curr = dummyNode
        
        while heap:
            value, index, node = heapq.heappop(heap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(heap, [node.val, index, node])
        
        return dummyNode.next
