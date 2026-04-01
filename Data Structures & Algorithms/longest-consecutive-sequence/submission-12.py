class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        i = 0
        res = 0

        while i < len(nums):
            n = nums[i]
            length = 1
            while n + 1 in numSet:
                length += 1
                n = n + 1
            res = max(res, length)
            i += 1
        
        return res




        