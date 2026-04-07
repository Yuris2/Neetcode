class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        l,r = 0,0
        jumps = 0

        while r < goal:
            maxJump = 0

            for j in range(l,r + 1):
                maxJump = max(maxJump, nums[j] + j)
            
            l = r + 1
            r = maxJump
            jumps += 1
        
        return jumps

        