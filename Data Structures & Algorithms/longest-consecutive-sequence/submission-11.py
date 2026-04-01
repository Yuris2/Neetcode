class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        res = 0

        l = 0

        for n in nums:
            length = 0
            if (n - 1) not in numSet:
                while n in numSet:
                    length += 1
                    n += 1
                res = max(res, length)
        
        return res






        