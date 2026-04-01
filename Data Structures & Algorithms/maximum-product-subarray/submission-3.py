class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMin = 1
        currentMax = 1
        res = -2e9

        for n in nums:
            tmp = currentMax * n
            currentMax = max(n, currentMax * n, currentMin * n)
            currentMin = min(tmp, currentMin * n, n)
            res = max(currentMax, res)

        return res

        