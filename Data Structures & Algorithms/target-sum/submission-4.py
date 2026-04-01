class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def backtrack(i, total):
            #We checked every number
            if i >= len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (i,total) in cache:
                return cache[i,total]
            
            addNumber = backtrack(i + 1, total + nums[i])
            subNumber = backtrack(i + 1, total - nums[i])

            res = addNumber + subNumber
            cache[i,total] = res

            return cache[i,total]
        
        return backtrack(0,0)

        