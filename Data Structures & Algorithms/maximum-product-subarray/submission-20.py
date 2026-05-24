class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd, minProd = 1,1
        res = -2e9

        for n in nums:
            tmp = minProd * n
            minProd = min(minProd * n, n, maxProd * n)
            maxProd = max(maxProd * n, n, tmp)

            res = max(maxProd, res)
        
        return res



        