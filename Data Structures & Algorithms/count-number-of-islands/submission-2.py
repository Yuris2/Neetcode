class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numOfIslands = 0;
        r = len(grid)
        c = len(grid[0])

        def dfs(x, y):
            #Check is coordinates are not out of bounds
            if x < 0 or x >= r or y < 0 or y >= c or grid[x][y] != '1':
                return
            else:
                #Destroy Island To mark as seen
                grid[x][y] = '0'
                dfs(x,y - 1)
                dfs(x,y + 1)
                dfs(x - 1,y)
                dfs(x + 1,y)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    numOfIslands += 1
                    #Count the surrounding land 
                    dfs(i, j)
        
        return numOfIslands

        