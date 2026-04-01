class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R,C = len(grid), len(grid[0])
        seen = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return 
            if (r,c) in seen or grid[r][c] != '1':
                return 
            
            seen.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r-1,c)

        res = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1' and (r,c) not in seen:
                    res += 1
                    dfs(r,c)
        return res
        