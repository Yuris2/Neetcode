class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums)
        res = 0

        def dp(i):
            if i >= len(nums) - 1:
                return 0
            #Can't go down 
            if nums[i] == 0:
                return 2e9
            
            res = 2e9
            for n in range(1,nums[i] + 1):
                res = min(dp(i + n), res)
            
            return 1 + res
        
        return dp(0)

        