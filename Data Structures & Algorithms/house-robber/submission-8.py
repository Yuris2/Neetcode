class Solution:
    def rob(self, nums: List[int]) -> int:
        #Rob from houses
        #Can't rob from two adjacent houses
        #Want to return max money
        cache = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i] + dp(i + 2), dp(i + 1))
            return cache[i]
        
        return dp(0)
        