class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {} # Maps number to an index
        for index in range(len(nums)):
            num = nums[index]
            if target - num in indexMap: # Checks if difference in hash
                return [indexMap[target - num], index]
            else: # Add number to hash 
                indexMap[num] = index

