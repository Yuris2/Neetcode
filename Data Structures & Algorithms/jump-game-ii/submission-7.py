class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        res = 0

        l, r = 0,0

        while r < goal:
            maxJump = 0

            for j in range(l, r + 1):
                jump = nums[j] + j
                maxJump = max(maxJump, jump)

            l = r + 1
            r = maxJump
            res += 1
        
        return res
        