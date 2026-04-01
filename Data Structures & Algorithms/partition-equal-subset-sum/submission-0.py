class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        target = total // 2

        cache = {}

        def backtrack(i, current_sum):
            if current_sum == target:
                return True
            if i >= len(nums):
                return False
            if (i, current_sum) in cache:
                return cache[(i, current_sum)]
            
            cache[(i, current_sum)] = backtrack(i + 1, current_sum + nums[i]) or backtrack(i + 1, current_sum)
        
            return cache[(i, current_sum)]
        return backtrack(0,0)
            

        