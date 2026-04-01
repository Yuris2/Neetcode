class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        target = total // 2

        cache = {}
        def dp(i, sum):
            if i >= len(nums):
                return False
            if (i, sum) in cache:
                return cache[(i, sum)]
            if sum == target:
                return True
            
            res = dp(i + 1, sum) or dp(i + 1, sum + nums[i])
            cache[(i,sum)] = res

            return res
        
        return dp(0,0)
        