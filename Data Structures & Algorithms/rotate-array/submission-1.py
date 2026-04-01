class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Trick is reverse Array
        #Reverse first k elements
        #Reverse rest of elements
        k = k % len(nums)

        if k == 0:
            return nums 
        
        def reverseArray(l,r):
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp

                l += 1
                r -= 1
        
        reverseArray(0, len(nums) - 1)
        reverseArray(0, k - 1)
        reverseArray(k, len(nums) - 1)
        