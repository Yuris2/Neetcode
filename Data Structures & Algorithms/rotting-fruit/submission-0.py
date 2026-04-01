class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        fresh = 0
        time = 0
        q = []

        for i in range(rows):
            for j in range(columns):
                coord = grid[i][j]

                if coord == 1:
                    fresh += 1
                elif coord == 2:
                    q.append([i,j])
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while fresh > 0 and q:
            n = len(q)

            for i in range(n):
                coord = q.pop(0)
                r, c = coord[0], coord[1]

                #Check in all coordinate directions

                for dr, dc in directions:
                    row, column = r + dr, c + dc

                    if (row < 0 or row >= rows or column < 0 or column >= columns or grid[row][column] != 1):
                        continue
                    
                    fresh -= 1
                    q.append([row, column])
                    grid[row][column] = 2
                    
            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1



        