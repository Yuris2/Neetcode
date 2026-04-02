class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -2e9
        minP, maxP = 1, 1
        for n in nums:
            tmp = maxP
            maxP = max(n, maxP * n, minP * n)
            minP = min(n, minP * n, tmp * n)

            res = max(res, maxP)
        
        return res

            


        