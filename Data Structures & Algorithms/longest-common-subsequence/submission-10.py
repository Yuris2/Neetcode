class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #Pattern
            #2D-DP tracking index, length, and order of chars w/binary choice
        
        #General Idea
            #If text1[i] == text2[j]: add 1 to length and check next possibility
            #Else
                #Return the max between skipping a letter in text1 and text2
            #dp[i][j] = max subsequence from text[i:] and text2[j:]
        n,m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        return dp[0][0]
