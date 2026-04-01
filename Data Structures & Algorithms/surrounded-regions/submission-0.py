class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        #Find unsurrounded coordinates. replace them with a temp variable
        def capture(r,c):
            if r < 0 or c < 0 or r >= ROW or c >= COL:
                return 
            elif grid[r][c] != 'O':
                return
            
            grid[r][c] = '#'

            capture(r + 1,c)
            capture(r - 1,c)
            capture(r,c + 1)
            capture(r,c - 1)
        
        #Replacing all Unsurrounded Coordinates with a protection
        for r in range(ROW):
            for c in range(COL):
                #Only checking the edges
                if (r in [0, ROW - 1] or c in [0, COL - 1]) and grid[r][c] == 'O':
                    capture(r,c)

        #Replacing unprotected O with X (Capture)        
        for r in range(ROW):
            for c in range(COL):
                #Only checking the edges
                if grid[r][c] == 'O':
                    grid[r][c] = 'X'
        
        for r in range(ROW):
            for c in range(COL):
                #Only checking the edges
                if grid[r][c] == '#':
                    grid[r][c] = 'O'