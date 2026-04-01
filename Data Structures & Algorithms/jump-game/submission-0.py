class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1

        for i in range(goal, -1, -1):
            maxJump = nums[i]
            #If we can jump to the goal by combining our jump and our index
            if maxJump + i >= goal:
                goal = i


        return goal == 0      