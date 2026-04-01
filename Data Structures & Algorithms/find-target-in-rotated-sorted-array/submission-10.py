class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minPoint = 0
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        minPoint = r

        if minPoint == 0:
            l, r = 0, len(nums) - 1
        if target >= nums[minPoint] and target <= nums[-1]:
            l, r = minPoint, len(nums) - 1
        else:
            l, r = 0, minPoint - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1


        