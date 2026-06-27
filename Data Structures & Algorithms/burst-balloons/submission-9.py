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
            
            for i in range(l + 1,r):
                c = nums[l] * nums[i] * nums[r]
                c += dp(l,i) + dp(i,r)
                res = max(res, c)
            
            cache[(l,r)] = res
            return res
        
        return dp(0, len(nums) - 1)

            

        