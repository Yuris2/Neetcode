class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        R, C = m, n
        cache = {}
        def dfs(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return 0
            if r == R - 1 and c == C - 1:
                return 1
            if (r,c) in cache:
                return cache[(r,c)]
            
            count = 0
            count += dfs(r + 1,c) + dfs(r, c + 1)

            cache[(r,c)] = count
            return count
        
        return dfs(0,0)
        