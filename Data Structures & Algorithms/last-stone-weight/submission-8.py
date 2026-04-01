import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #1. Create a max heap with all the stones
        #2. Pop the two heaviest stones
        #3. Compare Stones.
        #4a if x == y, continue iteration
        #4b if x < y, take difference add add onto heap
        #5  continue until there is either one or no stones left

        #1. 
        #turn into max heap
        stones = [-n for n in stones]
        heapq.heapify(stones)

        #5. REMEMBER NEGATIVE NUMBERS
        while len(stones) > 1:
            #2.
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            #4.
            if y < x:
                heapq.heappush(stones, y - x)
        
        if stones:
            return -stones[0]
        else:
            return 0
        