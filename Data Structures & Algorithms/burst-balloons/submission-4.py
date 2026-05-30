class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}

        #Think about in terms of the last balloon
        def dp(i,j):
            if i > j:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            
            res = 0
            for n in range(i + 1,j):
                val = nums[n]  * nums[i] * nums[j] + dp(i,n) + dp(n,j)
                res = max(res, val)
            
            cache[(i,j)] = res
            return res
        
        return dp(0,len(nums) - 1)

            


        