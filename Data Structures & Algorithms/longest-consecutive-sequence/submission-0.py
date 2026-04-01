class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        res = 0

        for n in nums:
            #If n is the start of a sequence
            #value that is one less is not in set

            if (n - 1) not in numSet:
                seqLen = 1
                while (n + 1) in numSet:
                    seqLen += 1
                    n += 1
                
                res = max(res, seqLen)
        
        return res