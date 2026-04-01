class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in nums:
            #start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while n in numSet:
                    length += 1
                    n += 1
                
                res = max(length, res)
        
        return res
        