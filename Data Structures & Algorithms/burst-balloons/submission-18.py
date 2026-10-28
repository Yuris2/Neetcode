class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = [[-1] * len(nums) for _ in range(len(nums))]

        def dp(l,r):
            if l > r:
                return 0
            if cache[l][r] != -1:
                return cache[l][r]
            
            res = 0
            for i in range(l + 1, r):
                val = nums[l] * nums[i] * nums[r]
                val += dp(l,i) + dp(i,r)
                res = max(val, res)
        
            cache[l][r] = res
            return res

        return dp(0, len(nums) - 1)

        