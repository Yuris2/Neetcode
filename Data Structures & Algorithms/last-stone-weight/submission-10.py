import collections

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y, x = heapq.heappop(stones), heapq.heappop(stones)
            #negative
            if (y < x):
                heapq.heappush(stones, (y - x))
        
        if stones:
            return -stones[0]
        else:
            return 0

        