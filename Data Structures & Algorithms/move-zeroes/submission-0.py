class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(l,r):
            tmp = nums[r]
            nums[r] = nums[l]
            nums[l] = tmp
        
        i = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                swap(i,r)
                i += 1
  
        