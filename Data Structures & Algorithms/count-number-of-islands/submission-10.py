class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if r < 0 or c < 0 or c >= C or r >= R:
                return 
            elif (r,c) in visited or grid[r][c] != '1':
                return
            
            visited.add((r,c))

            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)
        
        num = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1' and (r,c) not in visited:
                    num += 1
                    dfs(r,c)
        
        return num
        