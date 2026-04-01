# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummyNode = ListNode()
        curr = dummyNode

        for i in range(len(lists)):
            heap.append([lists[i].val, i, lists[i]])
        
        heapq.heapify(heap)

        while heap:
            val, idx, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next
            node = node.next

            if node:
                heapq.heappush(heap, [node.val, idx, node])
        
        return dummyNode.next
        