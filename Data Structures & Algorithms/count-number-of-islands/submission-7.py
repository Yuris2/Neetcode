class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        numOfIslands = 0

        def dfs(x,y):
            #Check if the coordinates are in bounds and are not water
            if x < 0 or x >= ROWS or y < 0 or y >= COLUMNS or grid[x][y] != '1':
                return
            else:
                grid[x][y] = '0'
                dfs(x - 1,y)
                dfs(x + 1,y)
                dfs(x,y -1 )
                dfs(x,y + 1)




        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == '1':
                    numOfIslands += 1
                    #Do something to ensure that nothing else is counted
                    dfs(i, j)
        
        return numOfIslands






        