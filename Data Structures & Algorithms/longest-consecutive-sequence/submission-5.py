class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)

        for n in nums:
            length = 1
            #Start of a sequence
            if (n - 1) not in numSet:
                while (n + 1) in numSet:
                    length += 1
                    n += 1
            
            res= max(res, length)
        
        return res
        