class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            st1 = -heapq.heappop(stones)
            st2 = -heapq.heappop(stones)

            if st1 > st2:
                newStone = st2 - st1

                heapq.heappush(stones, newStone)
        
        stones.append(0)
        return abs(stones[0])
        





        