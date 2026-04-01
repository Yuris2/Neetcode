class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        if totalSum % 2 != 0:
            return False
        
        target = totalSum // 2

        cache = {}
        def dp(i,total):
            if i >= len(nums):
                if total == target:
                    return True
                else:
                    return False
            if (i,total) in cache:
                return cache[(i,total)]
            
            res = dp(i + 1, total + nums[i]) or dp(i + 1, total)
            cache[(i,total)] = res

            return res

        return dp(0,0)            

        