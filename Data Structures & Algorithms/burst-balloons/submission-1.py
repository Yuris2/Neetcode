class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}
        def dp(i,j):
            if i > j:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            
            res = 0
            for k in range(i + 1,j):
                c = nums[i] * nums[k] * nums[j] + dp(i,k) + dp(k,j)
                res = max(res, c)
            
            cache[(i,j)] = res
            return res
        
        return dp(0,len(nums) - 1)

        