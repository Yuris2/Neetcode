class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        goal = len(nums) - 1
        #While we have not reached the goal
        while r < goal:
            #Farthest Jump that we can take
            farthest = 0
            #Iterate through each number in our window
            for i in range(l,r + 1):
                #Find the max jump
                farthest = max(farthest, i + nums[i])
            #Update pointers and add a layer
            l = r + 1
            r = farthest
            res += 1
        return res

        