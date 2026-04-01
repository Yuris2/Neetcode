class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numOfIslands = 0
        ROWS = len(grid)
        COLUMNS = len(grid[0])

        def dfs(x,y):
            #Ensure that coordinate is in bounds
            #Or that the coordiante is not water
            if x < 0 or x >= ROWS or y < 0 or y >= COLUMNS or grid[x][y] == '0':
                return
            #Water is found
            else:
                #Destroy island
                grid[x][y] = '0'
                #Check surroundings
                dfs(x - 1,y)
                dfs(x + 1,y)
                dfs(x,y - 1)
                dfs(x,y + 1)



        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == '1':
                    numOfIslands += 1
                    #Check surrounding islands
                    dfs(i,j)
        
        return numOfIslands
        