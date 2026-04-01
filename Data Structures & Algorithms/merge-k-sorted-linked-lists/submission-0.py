# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)

        #Get each val, rel position on list, and node and put onto the heap
        for i in range(len(lists)):
            node = lists[i]
            heapq.heappush(heap, [node.val, i, node])
        
        dummy = ListNode()
        cur = dummy
        
        #Should be sorted from decreasing order
        while heap:
            val,i, node = heapq.heappop(heap)
            cur.next = node
            cur = node
            node = node.next
            if node:
                heapq.heappush(heap, [node.val, i, node])
        
        return dummy.next

        