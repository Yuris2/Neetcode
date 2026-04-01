class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currSum = 0

        for n in nums:
            #Adding number to currSum
            currSum += n
            #Max sum vs currSum 
            res = max(res, currSum)
            #We don't want to continue the subarray
            if currSum < 0:
                currSum = 0

        return res
        