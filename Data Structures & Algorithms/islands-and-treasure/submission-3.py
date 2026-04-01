import collections

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen = set()
        def isValid(r,c):
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] < 0:
                return False
            if (r,c) in seen:
                return False
            return True
            
        R,C = len(grid), len(grid[0])

        queue = deque()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    seen.add((r,c))
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        distance = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()

                for delta_r, delta_c in directions:
                    new_row = r + delta_r
                    new_col = c + delta_c

                    if isValid(new_row, new_col):
                        queue.append((new_row, new_col))
                        seen.add((new_row, new_col))
                
                grid[r][c] = distance
            distance += 1


        