class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        res = -2e9

        for n in nums:
            currentSum += n
            res = max(currentSum, res)

            if currentSum < 0:
                currentSum = 0
        
        return res
        