class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L,R = i + 1, len(nums) - 1

            while L < R:
                ans = nums[L] + nums[R] + nums[i]

                if ans > 0:
                    R -= 1
                elif ans < 0:
                    L += 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

        return res                
        