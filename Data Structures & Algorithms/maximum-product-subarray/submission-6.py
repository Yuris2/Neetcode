class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -2e9
        minProduct, maxProduct = 1,1


        for n in nums:
            tmp = maxProduct * n
            maxProduct = max(maxProduct * n, minProduct * n, n)
            minProduct = min(minProduct * n, tmp, n)

            res = max(maxProduct, res)
        
        return res