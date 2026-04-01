class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(h):
            if h >= len(nums):
                return 0
            if h in cache:
                return cache[h]
            
            cache[h] =  max(nums[h] + dfs(h + 2), dfs(h + 1))
            return cache[h]
        
        return dfs(0)
        