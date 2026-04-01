class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])

        q = []
        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 1:
                    fresh += 1
                
                if grid[r][c] == 2:
                    q.append([r,c])
        
        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        while q and fresh > 0:
            n = len(q)

            for i in range(n):
                row, column = q.pop(0)

                #Check around for surrounding fruits
                for dr, dc in directions:
                    r = row + dr
                    c = column + dc

                    if r < 0 or r >= ROWS or c < 0 or c >= COLUMNS or grid[r][c] != 1:
                        continue
                    
                    fresh -= 1
                    grid[r][c] = 2
                    q.append([r,c])
                
            time += 1
        
        if fresh == 0:
            return time   
        else:
            return -1
        