class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = 1
        currMax = 1
        res = -2e9

        for n in nums:
            tmp = currMax * n
            currMax = max(currMax * n, currMin * n,n)
            currMin = min(currMin * n, tmp, n)

            res = max(currMax, res)
        
        return res
        