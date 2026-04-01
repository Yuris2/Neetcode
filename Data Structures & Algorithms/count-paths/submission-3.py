class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        R, C = m,n
        cache = {}

        def backtrack(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            if r == R - 1 and c == C - 1:
                return 1
            
            cache[(r,c)] = backtrack(r + 1, c) + backtrack(r, c + 1)

            return cache[(r,c)]
        
        return backtrack(0,0)
        