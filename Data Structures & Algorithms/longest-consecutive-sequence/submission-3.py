class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in nums:
            #Check if element is the start of seq
            if n - 1 not in numSet:
                length = 1
                while n + 1 in numSet:
                    length += 1
                    n += 1
        
                res = max(length, res)
        
        return res

        