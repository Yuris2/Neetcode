class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct, minProduct = 1,1
        res = -2e9

        for n in nums:
            tmp = maxProduct * n
            maxProduct = max(maxProduct * n, minProduct * n, n)
            minProduct = min(minProduct * n, tmp, n)

            res = max(maxProduct, res)
        
        return res
        