class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        cache = {}

        def dp(i,last):
            if i >= len(nums) or (last and i == len(nums) - 1):
                return 0
            if (i,last) in cache:
                return cache[(i,last)]
            
            cache[(i,last)] = max(dp(i + 2, last) + nums[i], dp(i + 1, last))
            return cache[(i,last)]
        
        return max(dp(0,True), dp(1, False))

        