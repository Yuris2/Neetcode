class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = -2e9
        curMax = 1
        curMin = 1

        for n in nums:
            tmp = curMax * n
            #Extend subarray, neg * min, or start fresh
            curMax = max(curMax * n, curMin * n, n)
            #Extend Subarray, max * negative or start fresh
            curMin = min(curMin * n, tmp, n)
            res = max(curMax, res)
        
        return res
            