import collections

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        queue = deque()
        seen =set()

        #Finding treasure
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    seen.add((r,c))
        
        def valid(row, col):
            if row < 0 or col < 0 or row >= ROW or col >= COL:
                return False
            elif grid[row][col] == -1 or (row,col) in seen:
                return False
            return True
        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        distance = 0
        #Running DFS on all of the treasures
        while queue:
            n = len(queue)
            for i in range(n):
                row, col = queue.popleft()
                grid[row][col] = distance
                
                for delta_row, delta_col in directions:
                    new_row = delta_row + row
                    new_col = delta_col + col

                    if not valid(new_row, new_col):
                        continue
                    queue.append((new_row, new_col))
                    seen.add((new_row, new_col))
            distance += 1



        