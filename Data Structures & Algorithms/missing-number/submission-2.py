class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #XORing numbers together results in 0
        res = len(nums)

        #If we xor, i ([0,n]) and the number in the array
        #No matter what order the number appears in the array
        #It will be XORed to 0, if exists.
        for i in range(len(nums)):
            #XORing
            res ^= i ^ nums[i]
        
        return res
        

