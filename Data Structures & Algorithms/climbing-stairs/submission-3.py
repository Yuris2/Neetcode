class Solution:
    def climbStairs(self, n: int) -> int:
        #BC
        #return n if less than or equal to 3
        if n <= 3:
            return n
        
        #Counting number of stairs
        dp = [0] * n

        dp[0] = 1
        dp[1] = 2
        dp[2] = 3

        #Number of jumps at an index
        #Sum of i - 2 and i - 1
        for i in range(3, n):
            #Populating dp
            dp[i] = dp[i - 2] + dp[i - 1]
        
        return dp[n - 1]



        