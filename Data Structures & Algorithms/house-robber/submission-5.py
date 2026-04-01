class Solution:
    def rob(self, nums: List[int]) -> int:
        #Two choices, we can rob this house and the i + 1 house
        #We can rob the next house
        cache = {}
        def backtrack(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i] +backtrack(i + 2), backtrack(i + 1))
            return cache[i]
        
        return backtrack(0)