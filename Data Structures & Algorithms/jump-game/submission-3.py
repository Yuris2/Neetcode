class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Approach
        #1. See if we can jump to the last index (goal)
        #2. Check the array backwards
        #3. At a given index, if we can jump to our current goal
        #4. see if we can jump to that index
        #5. Complete if the goal is at the start
        
        #1.
        goal = len(nums) - 1
        #2.
        for i in range(len(nums) - 1, -1, -1):
        #3.
            maxJump = nums[i] + i
        #4.
            if maxJump >= goal:
                goal = i
        #5.
        return goal == 0
            

        