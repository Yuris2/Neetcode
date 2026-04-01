class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def back(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                return 0
            if (i, total) in cache:
                return cache[(i, total)]
            
            add = back(i + 1, total + nums[i])
            sub = back(i + 1, total - nums[i])

            cache[(i, total)] = add + sub

            return cache[(i, total)]
        
        return back(0,0)
        