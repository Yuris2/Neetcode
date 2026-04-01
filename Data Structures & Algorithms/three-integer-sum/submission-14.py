class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                ans = num + nums[l] + nums[r]

                if ans > 0:
                    r -= 1
                elif ans < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])

                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res
                    
