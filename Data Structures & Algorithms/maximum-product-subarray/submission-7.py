class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -2e9

        maxProduct = minProduct = 1

        for num in nums:
            tmp = maxProduct * num
            maxProduct = max(maxProduct * num, minProduct * num, num)
            minProduct = min(minProduct * num, tmp, num)
        
            res = max(res, maxProduct)
        
        return res
