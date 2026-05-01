class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = {}
        
        def dp(i, start):
            if i >= len(nums) or (i == len(nums) - 1 and start):
                return 0
            if (i, start) in cache:
                return cache[(i,start)]
            
            res = max(dp(i + 1, start), nums[i] + dp(i + 2, start))
            cache[(i,start)] = res
            return res
        
        return max(dp(0, True), dp(1, False))
        