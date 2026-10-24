class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        cache = {}
        
        def dp(i,front):
            if i >= len(nums) or (i == len(nums) - 1 and front):
                return 0
            if (i,front) in cache:
                return cache[(i,front)]
            
            c1 = nums[i] + dp(i + 2, front)
            c2 = dp(i + 1, front)

            cache[(i,front)] = max(c1,c2)
            return cache[(i,front)]
        
        return max(dp(0,True), dp(1,False))


        