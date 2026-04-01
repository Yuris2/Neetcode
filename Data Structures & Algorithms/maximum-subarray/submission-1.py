class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Brute force approach
        
        res =  -2e9
        currSum = 0

        for n in nums:
            currSum += n
            res = max(currSum, res)
            #We will stop extending subarray if sum of curr window < 0
            if currSum < 0:
                currSum = 0
        
        return res
            
        