class Solution:
    def climbStairs(self, n: int) -> int:
        #Bottom Up Tabulation

        if n <= 3:
            return n
        
        dp = [0] * n

        dp[0] = 1
        dp[1] = 2
        dp[2] = 3

        for i in range(3, n):
            dp[i] = dp[i - 2] + dp[i - 1]
        
        return dp[n - 1]
        