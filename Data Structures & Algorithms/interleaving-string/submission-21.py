class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #Pattern
            #2D-DP with binary decisions

        #General Idea
            #Choose either s1[i] or s2[j] and see if you can form s3[i + j]
            #until you reach the end
            #dp[i][j] represents if you can form s3[i + j] from s1 and s3
        
        n,m = len(s1), len(s2)

        if n + m != len(s3):
            return False
        
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = True

        #Have to cover cases where there is still letters
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i < n and s1[i] == s3[i + j]:
                    dp[i][j] = dp[i + 1][j]
                if j < m and s2[j] == s3[i + j]:
                    dp[i][j] = dp[i][j] or dp[i][j + 1]
        
        return dp[0][0]
        