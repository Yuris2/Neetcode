class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        r = len(grid)
        c = len(grid[0])

        def dfs(x, y):
            #Check if in possible bounds and if the it is not water
            if x < 0 or x >= r or y < 0 or y >= c or grid[x][y] == '0':
                return
            else:
                grid[x][y] = '0'
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    res += 1
                    #Check connecting islands
                    dfs(i,j)
        return res
        