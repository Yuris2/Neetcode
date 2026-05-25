class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for n in nums:
            if n - 1 not in numSet:
                curLength = 1
                while n + curLength in numSet:
                    curLength += 1
                longest = max(longest, curLength)
        
        return longest
        
                