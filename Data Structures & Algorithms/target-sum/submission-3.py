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
        
            addNext = backtrack(i + 1, total + nums[i])
            subNext = backtrack(i + 1, total - nums[i])

            res = addNext + subNext
            cache[(i, total)] = res
            return cache[(i, total)]
        
        return backtrack(0,0)
        