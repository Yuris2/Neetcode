class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dp(i, prevValue):
            if i >= len(nums):
                return 0
            if (i, prevValue) in cache:
                return cache[(i, prevValue)]
            
            #Two Choices
            res = 0
            #Use Current Value
            if nums[i] > prevValue:
                res += 1 + dp(i + 1, nums[i])
                #CurrentValue has to Be Greater than the prevValue
            #Use Next Value
            res = max(res, dp(i + 1, prevValue))
                #Start a new Subsequence
            cache[(i, prevValue)] = res
            return res
        
        return dp(0, -2e9)
        
        