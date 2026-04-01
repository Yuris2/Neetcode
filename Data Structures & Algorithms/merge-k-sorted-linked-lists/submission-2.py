# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import collections
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)

        for i in range(len(lists)):
            node = lists[i]
            heapq.heappush(heap, [node.val, i, node])
        
        dummyNode = ListNode()
        cur = dummyNode

        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = node
            node = node.next
            if node:
                heapq.heappush(heap, [node.val, i, node])
        
        return dummyNode.next

        