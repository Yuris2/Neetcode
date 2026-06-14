class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s), len(t)

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = 1

        for i in range(n - 1, -1, -1):
            dp[i][-1] = 1
            for j in range(m - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
                dp[i][j] += dp[i + 1][j]
        
        return dp[0][0]
        def dp(i,j):
            if j >= m:
                return 1
            if i >= n:
                return 0
            
            res = 0
            if s[i] == t[j]:
                res += dp(i + 1, j + 1)
            res += dp(i + 1, j)

            return res
        
        return dp(0,0)
        