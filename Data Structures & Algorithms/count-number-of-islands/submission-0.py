class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        res = 0

        def dfs(x,y):
            #If the coordinates are not out of bounds or water is found
            if x < 0 or x >= r or y < 0 or y >= c or grid[x][y] != '1':
                #Essentially pass and do nothing
                return
            else:
                #Turn seen grid to water marking it as seen
                grid[x][y] = '0'
                #Check all surrounding points
                dfs(x + 1 , y)
                dfs(x - 1 , y)
                dfs(x , y + 1)
                dfs(x , y - 1)


        for i in range(r):
            for j in range(c):
                #If we found an island
                if grid[i][j] == '1':
                    #Increment number of islands found
                    res += 1
                    #Check for all connecting land in the map
                    dfs(i,j)
        
        return res


        
        