class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -2e9
        runningSum = 0

        for n in nums:
            runningSum += n
            res = max(runningSum, res)

            if runningSum < 0:
                runningSum = 0
        
        return res
        