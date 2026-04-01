class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def back(i):
            if i >= len(cost):
                return 0
            if i in cache:
                return cache[i]

            #Min of taking current step, next step or skipping     
            return cost[i] + min(back(i + 1), back(i + 2))
        
        #We can start at step 0 or step1
        return min(back(0), back(1))
        