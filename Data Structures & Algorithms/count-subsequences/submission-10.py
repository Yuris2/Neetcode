class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s), len(t)
        cache = [[-1] * (m + 1) for _ in range(n + 1)]
        def dp(i,j):
            if j == m:
                return 1
            if i >= n:
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            
            res = dp(i + 1, j)

            if s[i] == t[j]:
                res += dp(i + 1, j + 1)
            
            cache[i][j] = res
            return res
        
        return dp(0,0)

        