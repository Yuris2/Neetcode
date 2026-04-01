import collections

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        seen = set()
        queue = deque()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    seen.add((r,c))
        
        distance = 0
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while queue:
            for n in range(len(queue)):
                r, c = queue.popleft()

                grid[r][c] = distance
                for delta_row, delta_col in directions:
                    newR, newC = r + delta_row, c + delta_col

                    if newR < 0 or newR >= ROW or newC < 0 or newC >= COL:
                        continue
                    elif (newR, newC) in seen or grid[newR][newC] == -1:
                        continue
                    seen.add((newR, newC))
                    queue.append((newR,newC))
            distance += 1
                    

                    


        