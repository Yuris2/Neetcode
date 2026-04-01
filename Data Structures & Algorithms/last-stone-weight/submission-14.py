import collections
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-n for n in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            #-6
            y = heapq.heappop(heap)
            #-4
            x = heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap, y - x)

        return -heap[0] if heap else 0
        