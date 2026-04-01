class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, total):
            if i >= len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (i, total) in cache:
                return cache[(i,total)]
            
            add = dfs(i + 1, total + nums[i])
            sub = dfs(i + 1, total - nums[i])

            cache[(i,total)] = add + sub

            return cache[(i,total)]
        
        return dfs(0,0)

                
                
        