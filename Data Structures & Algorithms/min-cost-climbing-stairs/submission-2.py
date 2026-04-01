class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def back(index):
            if index >= len(cost):
                return 0
            if index in cache:
                return cache[index]

            cache[index] = cost[index] + min(back(index + 1),back(index + 2))

            return cache[index]
        
        return min(back(0), back(1))
            

        