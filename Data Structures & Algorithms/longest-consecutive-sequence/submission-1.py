class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longestSeq = 0

        for n in nums:
            #Beginning of sequence
            if (n - 1) not in numSet:
                seq = 1

                while (n + 1) in numSet:
                    seq += 1
                    n += 1
                
                longestSeq = max(longestSeq, seq)
        
        return longestSeq
