import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-n for n in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, x - y )
        
        if stones :
            return -stones[0]
        else:
            return 0


        