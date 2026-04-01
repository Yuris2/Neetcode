class Solution:
    def canJump(self, nums):
      #Iterate through the back of the array
      #Find if any elements can jump that element
      #If any
        #Set the new goal equal to num where we jump to
    #[1,2,0,1,0]  

        n = len(nums)
        goal = n - 1

        for i in range(len(nums) -1 , -1, -1):
            maxJump = i
            if maxJump + nums[i] >= goal:
                goal = maxJump
            
        if goal != 0:
            return False
        
        return True
