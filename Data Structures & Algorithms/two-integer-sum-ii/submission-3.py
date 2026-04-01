class Solution:
    def twoSum(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l < r:
            currentSum = nums[l] + nums[r]

            if currentSum == target:
                return [l + 1, r + 1]
            elif currentSum > target:
                r -= 1
            else:
                l += 1
        
        return []