class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        #dp[i]
        cur = [0] * (m + 1)
        #dp[i + 1]
        prev = [0] * (m + 1)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    cur[j] = 1 + prev[j + 1]
                else:
                    #dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                    cur[j] = max(prev[j], cur[j + 1])
            
            prev = cur
            cur = [0] * (m + 1)
        
        return prev[0]
        