class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1), len(word2)
        cache = [[2e9] * (n + 2) for _ in range(m + 2)]
        
        def dp(i,j):
            if i >= n:
                return m - j
            if j >= m:
                return n - i
            if cache[i][j] < 2e9:
                return cache[i][j]
            
            if word1[i] == word2[j]:
                cache[i][j] = dp(i + 1, j + 1)
                return dp(i + 1, j + 1)
            
            delete = dp(i + 1, j)
            insert = dp(i, j + 1)
            replace = dp(i + 1, j + 1)

            cache[i][j] = 1 + min(delete,insert,replace)
            return cache[i][j]

        return dp(0,0)
        