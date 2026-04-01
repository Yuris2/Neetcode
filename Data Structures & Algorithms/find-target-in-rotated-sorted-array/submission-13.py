class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        #R pointer is index of minimum element
        if target <= nums[-1]:
            l,r = r, len(nums) - 1
        elif target >= nums[0]:
            l,r = 0, r - 1
        else:
            l,r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1
        