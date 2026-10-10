class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        #If we XOR each number from 0...n
        #And every element in the array
        #The missing number will be res
        for i,n in enumerate(nums):
            res ^= (n ^ i)
        
        return res

        