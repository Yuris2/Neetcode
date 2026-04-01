class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        #If the array was not rotated or rotation divisible by length
        if nums[l] < nums[r]:
            return nums[l]
        
        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        return nums[r]

        
        