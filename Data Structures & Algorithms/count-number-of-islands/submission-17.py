class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R,C = len(grid), len(grid[0])

        def dfs(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return
            if grid[r][c] != '1':
                return
            
            grid[r][c] = '#'
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        
        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r,c)
        return res
        