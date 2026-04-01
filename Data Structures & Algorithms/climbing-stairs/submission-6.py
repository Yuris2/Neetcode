class Solution:
    def climbStairs(self, n: int) -> int:
        #Approach
        # -At n, add the number of steps it takes to get to n -1 and n -2 
        # from 1 - 3 steps always 1 - 3 possibilities
        if n <= 3:
            return n
        
        steps = [0] * n
        steps[0] = 1
        steps[1] = 2
        steps[2] = 3
        #Addingu up the n possibilities
        for i in range(2, n):
            steps[i] = steps[i - 2] + steps[i - 1]
        
        return steps[n - 1]



        