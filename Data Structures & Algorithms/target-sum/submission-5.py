class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def backtrack(i, total):
            if i >= len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (i, total) in cache:
                return cache[(i,total)]
            
            add = backtrack(i + 1, nums[i] + total)
            sub = backtrack(i + 1, total - nums[i])

            res = add + sub
            cache[(i, total)] = res

            return res
        
        return backtrack(0,0)
        