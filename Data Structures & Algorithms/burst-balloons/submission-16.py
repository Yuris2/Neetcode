class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        cache = [[-1] * n for _ in range(n)]

        def dp(l,r):
            if l > r:
                return 0
            if cache[l][r] != -1:
                return cache[l][r]
             
            res = 0
            for c in range(l + 1, r):
                v = nums[l] * nums[c] * nums[r]
                v += dp(l,c) + dp(c,r)
                res = max(res, v)
            
            cache[l][r] = res
            return res
        
        return dp(0,len(nums) - 1)
        