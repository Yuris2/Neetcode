class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = {}
        def dfs(index):
            if index >= len(nums):
                return 0
            if index in cache:
                return cache[index]
            
            cache[index] = max(nums[index] + dfs(index + 2), dfs(index + 1))
            return cache[index]
        
        return dfs(0)