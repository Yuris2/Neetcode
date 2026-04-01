# read if each value in nums is equal to input 'val'
# initialize a writer for valid nums = 0
# if nums[read] is NOT equal to 'val', it is valid
# these should increase the write count
# overwriting provides for better time complexity as it's O(1)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
       