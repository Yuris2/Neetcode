class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0

        #[1,7,3,6,5,6]

        for i, n in enumerate(nums):
            totalSum = totalSum - n

            if totalSum == leftSum:
                return i
            
            leftSum += n
        
        return -1
            
        