class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        cache = {}
        def backtrack(i,j):
            if i == n:
                return m - j
            if j == m:
                return n - i
            if (i,j) in cache:
                return cache[(i,j)]

            if word1[i] == word2[j]:
                return backtrack(i + 1, j + 1)
            else:
                res = min(1 + backtrack(i + 1, j), 1 + backtrack(i, j + 1))
                res = min(res, 1 + backtrack(i + 1, j + 1))
                cache[(i,j)] = res
                return res
            
        
        return backtrack(0,0)
            
        