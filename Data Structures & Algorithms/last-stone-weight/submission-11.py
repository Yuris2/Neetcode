import collections

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, stone in enumerate(stones):
            stones[i] = -stone
        
        heapq.heapify(stones)

        while len(stones) > 1:
            #-5
            y = heapq.heappop(stones)
            #-4
            x = heapq.heappop(stones)

            if y < x:
                heapq.heappush(stones, y - x)
        
        if stones:
            return -stones[0]
        else:
            return 0


        