class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #Pattern
            #2D-DP with binary choices (skip/include)
        
        #Geenral Idea
            #Track indices of both s,t
            #If s[i] == t[j]: move to both letters
            #Include the result of skipping the current letter
            #DP[i][j] = number of ways to reach t[:j] from s[:i]
        
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        #Have to set the corner = 1
        dp[len(s)][len(t)] = 1

        for i in range(len(s) - 1, -1, -1):
            dp[i][-1] = 1
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
                dp[i][j] += dp[i + 1][j]
        
        return dp[0][0]

        