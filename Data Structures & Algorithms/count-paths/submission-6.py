class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def dp(r,c):
            if r >= m or c >= n or r < 0 or c < 0:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            if (r,c) in cache:
                return cache[(r,c)]

            cache[(r,c)] = dp(r + 1, c) + dp(r, c + 1)
            
            return cache[(r,c)]
        
        return dp(0,0)
        