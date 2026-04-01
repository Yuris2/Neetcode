class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        cache = {}
        def dfs(i, total):
            if i >= len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (i,total) in cache:
                return cache[(i,total)]
            
            add = dfs(i + 1, total + nums[i])
            subtract = dfs(i + 1, total - nums[i])

            cache[(i,total)] = add + subtract

            return cache[(i,total)]
        
        return dfs(0, 0)
            

        