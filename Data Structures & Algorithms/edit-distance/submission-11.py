class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1), len(word2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            dp[i][m] = n - i
        
        for j in range(m):
            dp[n][j] = m - j
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    ins = dp[i + 1][j]
                    de = dp[i][j + 1]
                    re = dp[i + 1][j + 1]

                    dp[i][j] = 1 + min(ins, de, re)
        
        return dp[0][0]