class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #money
        #monkey
        n,m = len(word1), len(word2)
        cache = [[2e9] * (m + 1) for _ in range(n + 1)]

        def dp(i,j):
            if i >= n:
                return m - j
            if j >= m:
                return n - i
            if cache[i][j] < 2e9:
                return cache[i][j]
            
            res = 2e9

            if word1[i] == word2[j]:
                res = dp(i + 1, j + 1)
            else:
                add = dp(i, j + 1)
                delete = dp(i + 1, j)
                skip = dp(i + 1, j + 1)

                res = 1 + min(add,delete,skip)
            
            cache[i][j] = res
            return res
        
        return dp(0,0)

        