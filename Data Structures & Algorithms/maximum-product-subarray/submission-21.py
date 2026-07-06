class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum, minimum = 1, 1
        res = -2e9

        for n in nums:
            tmp = maximum
            maximum = max(n, minimum * n, maximum * n)
            minimum = min(n, minimum * n, tmp * n)

            res = max(res, maximum)
        
        return res
        