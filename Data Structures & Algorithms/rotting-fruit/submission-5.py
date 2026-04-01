import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        queue = deque()
        time = 0
        fresh = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        
        def isValid(r,c):
            if r < 0 or c < 0 or r >= ROW or c >= COL:
                return False
            elif grid[r][c] != 1:
                return False 
            return True
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        #Run bfs on the graph
        while queue and fresh > 0:
            for i in range(len(queue)):
                row, col = queue.popleft()

                for delta_row, delta_col in directions:
                    new_row = delta_row + row
                    new_col = delta_col + col

                    if not isValid(new_row, new_col):
                        continue
                    
                    fresh -= 1
                    grid[new_row][new_col] = 2
                    queue.append((new_row,new_col))  
            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1
        
        