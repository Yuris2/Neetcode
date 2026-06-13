class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}

        def dp(l,r):
            if l > r:
                return 0
            if (l,r) in cache:
                return cache[(l,r)]
            
            res = 0
            for c in range(l + 1, r):
                val = nums[l] * nums[c] * nums[r]
                val += dp(l,c) + dp(c, r)
                res = max(res, val)
            
            cache[(l,r)] = res
            return res
        
        return dp(0, len(nums) - 1)


        