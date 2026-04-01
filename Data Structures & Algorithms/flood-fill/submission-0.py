class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R, C = len(grid), len(grid[0])

        originalColor = grid[sr][sc]

        if originalColor == color:
            return grid
        
        visited = set()
        def dfs(r, c):
            if r < 0 or c < 0 or c >= C or r >= R or grid[r][c] != originalColor or (r,c) in visited:
                return
            
            grid[r][c] = color
            visited.add((r,c))

            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)
        
        dfs(sr, sc)
        return grid


        