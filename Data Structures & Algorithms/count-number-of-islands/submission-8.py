class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Approach
        #1.  Iterate through every (x,y)
        #2a. If we hit water (0), pass over it
        #2b. If we hit land (1), increment number of islands by one
        #3b. Use dfs to destroy all of the land around it so we do not double count
        #4.  return number of islands
        R = len(grid)
        C = len(grid[0])

        def dfs(r, c):
            #check if coordinate is in bounds and is an islands
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] != '1':
                #skip iteration
                return
            #destroy islands
            grid[r][c] = '0'
            #checking coordinates around
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            
        num = 0
        #1
        for x in range(R):
            for y in range(C):
                #2b.
                if grid[x][y] == '1':
                    num += 1
                    #3b.
                    dfs(x, y)
        #4. 
        return num
        