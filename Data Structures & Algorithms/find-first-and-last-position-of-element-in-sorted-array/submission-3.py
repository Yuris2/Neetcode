class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)

        return [left, right]

    def binarySearch(self, nums, target, leftBias):
        l,r = 0, len(nums) - 1
        index = -1
        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                index = m

                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        
        return index

        