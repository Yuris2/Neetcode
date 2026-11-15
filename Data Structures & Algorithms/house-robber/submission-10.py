class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            
            #C1 = We don't rob this house
            #C2 = We rob this house (add to our total), rob the next next house
            cache[i] = max(dp(i + 1), nums[i] + dp(i + 2))
            return cache[i]
        
        return dp(0)
        