import collections
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Pattern:
            #Max-Heap
        
        #General Idea
            #Pop two stones from the max heap while len > 1
            #If x < y, add (y - x) to the max heap
            #Return 1 if len(heap) == 1 else 0
        
        stones = [-n for n in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x,y = heapq.heappop(stones), heapq.heappop(stones)

            if x < y:
                heapq.heappush(stones, x - y)
        
        if len(stones) == 1: 
            return -stones[0]
        return 0
            
                    