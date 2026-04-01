class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -2e9
        minProduct, maxProduct = 1,1

        for i in range(len(nums)):
            tmp = maxProduct * nums[i]
            maxProduct = max(maxProduct * nums[i], minProduct * nums[i], nums[i])
            minProduct = min(minProduct * nums[i], tmp, nums[i])

            res = max(res, maxProduct)
        
        return res
        