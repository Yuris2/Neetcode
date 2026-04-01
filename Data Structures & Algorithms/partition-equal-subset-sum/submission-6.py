class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 != 0:
            return False
        
        cache = {}
        def dfs(i, total):
            if total == target:
                return True
            if (i,total) in cache:
                return cache[(i,total)]
            
            if total > target or i >= len(nums):
                return False
            
            cache[(i,total)] = (dfs(i + 1, total + nums[i]) or dfs(i + 1, total))
        
            return cache[(i,total)]
            
        return dfs(0, target // 2)

        