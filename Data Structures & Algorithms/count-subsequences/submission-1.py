class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s), len(t)

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = 1

        for i in range(n - 1, -1, -1):
            #If we can reach the end of t
            dp[i][-1] = 1
            for j in range(m - 1, -1, -1):
                #If s[i] == t[j]:
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
                #Add the result with skipping s[i] (i + 1, j)
                dp[i][j] += dp[i + 1][j]
        
        return dp[0][0]
            


        