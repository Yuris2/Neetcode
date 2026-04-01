class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 == 1:
            return False
        
        cache = {}
        def dfs(i, count):
            if count == target:
                return True
            if i >= len(nums):
                return False
            if (i, count) in cache:
                return cache[(i,count)]
            
            cache[(i,count)] = dfs(i + 1, count + nums[i]) or dfs(i + 1, count)
            return cache[(i,count)] 
        
        return dfs(0, target // 2)

        