class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            maxJump = nums[i] + i
            if maxJump >= goal:
                goal = i
        
        return goal == 0
        