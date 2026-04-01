class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = r = 0
        goal = len(nums) - 1

        while r < goal:
            maxJump = 0

            for j in range(l,r + 1):
                maxJump = max(maxJump, nums[j] + j)
            
            l = r + 1
            r = maxJump
            jumps += 1
        
        return jumps
        