class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        n,m = len(word1), len(word2)
        def dp(i,j):
            if i == n:
                return m - j
            if j == m:
                return n - i
            if (i,j) in cache:
                return cache[(i,j)]
            
            if word1[i] == word2[j]:
                cache[(i,j)] = dp(i + 1, j + 1)
            else:
                r = dp(i + 1, j + 1)
                ip = dp(i + 1, j)
                d = dp(i, j + 1)

                cache[(i,j)] = 1 + min(r,ip,d)
            
            return cache[(i,j)]

        
        return dp(0,0)
        