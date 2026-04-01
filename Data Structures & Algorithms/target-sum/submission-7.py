class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0

        cache = {}
        def backtrack(i, total_sum):
            if i >= len(nums):
                if total_sum == target:
                    return 1
                else:
                    return 0
            if (i,total_sum) in cache:
                return cache[(i,total_sum)]
            
            
            
            add = backtrack(i + 1, total_sum + nums[i])
            sub = backtrack(i + 1, total_sum - nums[i])

            cache[(i,total_sum)] = add + sub

            return cache[(i,total_sum)]
        
        res += backtrack(0,0)
        return res
        