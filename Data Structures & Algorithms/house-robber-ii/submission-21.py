class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #Houses are arranged in a circle
        #Cannot rob two adjacent houses
            #Includes first and last index
                #Have to keep track on if you started from i=0
        
        cache = {}
        def dp(i, start):
            if i >= len(nums):
                return 0
            if start and i == len(nums) - 1:
                return 0
            if (i, start) in cache:
                return cache[(i, start)]
            
            choice1 = nums[i] + dp(i + 2, start)
            choice2 = dp(i + 1, start)
            cache[(i, start)] = max(choice1, choice2)

            return cache[(i, start)]
        #Choices
            #Rob the current house + sum of the result for (i + 2)
            #Skip the current house
        
        #Return the max between choice 1 and 2.
        return max(dp(0,True), dp(1, False))
        