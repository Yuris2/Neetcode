class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1), len(text2)
        cache = {}
        def dp(i,j):
            if i >= n:
                return 0
            if j >= m:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            
            res = 0
            if text1[i] == text2[j]:
                res = 1 + dp(i + 1, j + 1)
            else:
                res = max(dp(i, j + 1), dp(i + 1, j))

            cache[(i,j)] = res
            return res
        
        return dp(0,0)

        