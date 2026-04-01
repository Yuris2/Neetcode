class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        cache = {}

        def dfs(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return float('inf')
            elif r == R - 1 and c == C -1:
                return grid[r][c]
            if (r,c) in cache:
                return cache[(r,c)]
            
            count = grid[r][c]
            count += min(dfs(r + 1, c), dfs(r, c + 1))
            cache[(r,c)] = count
            return cache[(r,c)]
        
        return dfs(0,0)

            
        