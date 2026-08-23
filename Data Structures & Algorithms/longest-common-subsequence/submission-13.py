class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def dp(i,j):
            if i >= len(text1):
                return 0
            if j >= len(text2):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]

            
            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + dp(i + 1, j + 1)
            else:
                res = max(dp(i + 1, j), dp(i, j + 1))
                cache[(i,j)] = res
            
            return cache[(i,j)]
        
        return dp(0,0)
        