class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i, prevValue):
            if i >= len(nums):
                return 0
            if (i,prevValue) in cache:
                return cache[(i,prevValue)]
            
            res = 0
            if nums[i] > prevValue:
                res = 1 + dfs(i + 1, nums[i])
            res = max(res, dfs(i + 1, prevValue))

            cache[(i,prevValue)] = res

            return res
        
        return dfs(0, -2e9)
            
        