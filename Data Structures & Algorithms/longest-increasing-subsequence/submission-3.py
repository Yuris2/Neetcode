class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dp(i, prevValue):
            if i >= len(nums):
                return 0
            if (i, prevValue) in cache:
                return cache[(i, prevValue)]
            
            res = 0
            if prevValue < nums[i]:
                res = 1 + dp(i + 1, nums[i])
            
            res = max(res, dp(i + 1, prevValue))

            cache[(i, prevValue)] = res
            return res
        
        return dp(0, -2e9)
        