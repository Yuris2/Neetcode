class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -2e9
        maximum, minProduct = 1,1

        for n in nums:
            tmp = maximum * n
            maximum = max(maximum * n, minProduct * n, n)
            minProduct = min(minProduct * n, tmp, n)

            res = max(res, maximum)
        
        return res
        