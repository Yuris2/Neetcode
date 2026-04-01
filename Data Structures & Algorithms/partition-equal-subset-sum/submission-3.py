class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        if totalSum % 2 == 1:
            return False

        target = totalSum // 2

        def backtrack(i, amount):
            if i >= len(nums):
                if amount == 0:
                    return True
                return False
            
            return backtrack(i + 1, amount - nums[i]) or backtrack(i + 1, amount)
        
        return backtrack(0, target)
            


        