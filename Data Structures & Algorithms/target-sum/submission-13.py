class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dp(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                return 0

            if (i,total) in cache:
                return cache[(i, total)]
            
            c1 = dp(i + 1, total + nums[i])
            c2 = dp(i + 1, total - nums[i])

            cache[(i, total)] = c1 + c2
            return c1 + c2
        
        return dp(0,0)
        