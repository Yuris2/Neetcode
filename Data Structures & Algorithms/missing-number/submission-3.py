class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #XORing numbers together results in 0
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        
        return res
