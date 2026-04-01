class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        currSum = 0
        res = 0

        for n in nums:
            currSum += n

            #Can we chop away some prefix s.t currSum = k 
            if currSum - k in prefixSum: 
                res += prefixSum[currSum - k]
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
        
        return res
        