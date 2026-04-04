class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #Partition the array into two subsets
        #Sum(Subset1) == Sum(Subset2)
        if sum(nums) % 2 != 0:
            return False
            #Sum of array has to be even
        
        #We don't need to calculate which numbers are in each subset
        #Just whether or not we can partition it
        partitionVal = sum(nums) // 2

        cache = {}

        def dp(i, target):
            if target == 0:
                return True
            if (i,target) in cache:
                return cache[(i, target)]
            
            if i >= len(nums) or target < 0:
                return False

            res = dp(i + 1, target) or dp(i + 1, target - nums[i])
            cache[(i, target)] = res


            return res
        
        return dp(0, partitionVal)
