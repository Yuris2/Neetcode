class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        l = r = 0
        res = 0
        maxJump = 0

        while r < goal:
            for i in range(l,r + 1):
                maxJump = max(maxJump, nums[i] + i)
            l = r + 1
            r = maxJump
            res += 1
        
        return res
        

        