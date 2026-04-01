class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def back(i):
            if i >= len(cost):
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = cost[i] + min(back(i + 1), back(i + 2))
            return cache[i]
        
        return min(back(0), back(1))
        