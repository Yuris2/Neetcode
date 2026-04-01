class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l < r:
            res = nums[l] + nums[r]

            if res > target:
                r -= 1
            elif res < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        return []
        