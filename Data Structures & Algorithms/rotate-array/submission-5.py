class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        if k == 0:
            return nums
        
        def reverseArray(l,r):
            while l < r:
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp

                l += 1
                r -= 1
        
        reverseArray(0, len(nums) - 1)

        reverseArray(0, k - 1)

        reverseArray(k, len(nums) - 1)
        