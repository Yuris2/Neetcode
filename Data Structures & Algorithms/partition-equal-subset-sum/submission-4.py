class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        targetSum = sum(nums)

        if targetSum % 2 != 0:
            return False
        
        targetSum = targetSum // 2

        cache = {}
        def backtrack(i, target):
            if target == 0:
                return True
            if i >= len(nums):
                return False
            if (i, target) in cache:
                return cache[(i, target)]
            
            cache[(i, target)] = backtrack(i + 1, target - nums[i]) or backtrack(i + 1, target)

            return cache[(i, target)]
        
        return backtrack(0, targetSum)


            

        