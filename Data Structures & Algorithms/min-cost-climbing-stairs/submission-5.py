class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def back(i):
            if i >= len(cost):
                return 0
            #The min cost to reach a certain point at an index never changes
            if i in cache:
                return cache[i]
            
            cache[i] = cost[i] + min(back(i + 2), back(i + 1))
            #Two decisions. Take this step, take the next step. Have to take curr
            return cache[i]
        
        return min(back(0), back(1))
        