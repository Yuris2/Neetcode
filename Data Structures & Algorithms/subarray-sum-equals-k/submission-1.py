class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        res = 0
        currentSum = 0

        for n in nums:
            currentSum += n

            if currentSum - k in prefixSum:
                res += prefixSum[currentSum - k]
            
            prefixSum[currentSum] = 1 + prefixSum.get(currentSum,0)
        
        return res
        