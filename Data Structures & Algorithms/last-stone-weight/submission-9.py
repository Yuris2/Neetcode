import collections

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Convert to max heap by turning all of the values negative
        stones = [-n for n in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            #Remember they are negative values
            if y < x:
                newStone = y - x
                heapq.heappush(stones, newStone)
        
        if stones:
            return -stones[0]
        else:
            return 0
        