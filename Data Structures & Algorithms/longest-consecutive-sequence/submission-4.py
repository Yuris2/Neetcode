class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Convert nums into a set
        numSet = set(nums)
        res = 0

        for n in numSet:
            #Start of sequence is if n - 1 is not in the set
            if n - 1 not in numSet:
                length = 0
                while n in numSet:
                    #Increment length of sequence
                    length += 1
                    #Increment n by one
                    n += 1
                
                res = max(res, length)
        
        return res

        