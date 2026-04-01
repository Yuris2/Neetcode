class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #If the array has an odd sum, return False
        totalSum = sum(nums)
        
        if totalSum % 2 != 0:
            return False
        #We have to find a way to create a partition that adds up to half of the totalSum

        cache = {}
        def backtrack(i, total_sum):
            if total_sum == 0:
                return True
            if i >= len(nums):
                return False
            if (i, total_sum) in cache:
                return cache[(i, total_sum)]
            
            #Two choices, add nums[i], skip nums[i]
            res = (backtrack(i + 1, total_sum - nums[i]) or 
            backtrack(i + 1, total_sum))

            cache[(i, total_sum)] = res

            return res
        
        return backtrack(0, totalSum // 2)
           

        
            

        