class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            ans = nums[l] + nums[r]

            if ans > target:
                r -= 1
            elif ans < target:
                l += 1
            else:
                return [l+1,r+1]
        
        return [-1,-1]


        