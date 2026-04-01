class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        if len(nums) == 1:
            return nums[0]
        def dp(i, start):
            if i >= len(nums):
                return 0
            if start and i == len(nums) - 1:
                return 0
            if (i, start) in cache:
                return cache[(i,start)]
            
            res = max(nums[i] + dp(i + 2, start), dp(i + 1, start))
            cache[(i,start)] = res

            return res
        
        return max(dp(0,True), dp(1, False))
        