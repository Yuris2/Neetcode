class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        res = 0
        pre = 0

        for num in nums:
            pre += num
            if pre - k in prefixSum:
                res += prefixSum[pre - k]
            prefixSum[pre] = 1 + prefixSum.get(pre, 0)
        
        return res
        