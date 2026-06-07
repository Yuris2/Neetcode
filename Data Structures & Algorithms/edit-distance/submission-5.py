class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #Pattern
            #2D-DP where you have 3 choices and bc is when you reach end of one wor
        #General Idea
            #Track indices, if w1[i] == w2[j] requires no transformations
            #else: take the minimum of 3 choices
            #Return remaining other chars when you reach the end of 1 string
            #dp[i][j] = min number of ops to make w1[:i] to w2[:j]
        n,m = len(word1), len(word2)

        dp = [[2e9] * (m + 1) for _ in range(n + 1)]

        for j in range(m + 1):
            dp[n][j] = m - j
        
        for i in range(n + 1):
            dp[i][m] = n - i
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    insert = dp[i][j + 1]
                    delete = dp[i + 1][j]
                    replace = dp[i + 1][j + 1]

                    dp[i][j] = 1 + min(insert, delete, replace)
        
        return dp[0][0]