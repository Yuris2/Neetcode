class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        if k == 0: return
        
        def reverseList(l,r):
            while l < r:
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp

                l += 1
                r -= 1
        
        reverseList(0, len(nums) - 1)

        reverseList(0, k - 1)

        reverseList(k, len(nums) - 1)

    

        