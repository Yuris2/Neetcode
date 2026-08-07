class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dp(i, prev):
            if i >= len(nums):
                return 0
            if (i,prev) in cache:
                return cache[(i,prev)]
            
            
            res = -2e9
            if nums[i] > prev:
                res = max(res, 1 + dp(i + 1, nums[i]))
            
            
            res = max(res, dp(i + 1, prev))
            cache[(i,prev)] = res
            return res
        
        return dp(0, -2e9)
            

        
        