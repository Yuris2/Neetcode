class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0, 1, 1, 2, 3]
        l = 1
        r = 1
        while r < len(nums):
            if nums[r] == nums[r - 1]:
                r += 1
            else:
                nums[l] = nums[r]
                l += 1
                r += 1
        return l

        

        

        