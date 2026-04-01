import collections

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R,C = len(grid), len(grid[0])
        seen = set()

        def isValid(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return False
            if grid[r][c] == -1 or (r,c) in seen:
                return False
            return True
        
        queue = deque()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    queue.append((r,c,0))
                    seen.add((r,c))
        
        directions = [[1,0],[-1,0], [0,1], [0, -1]]

        while queue:
            for _ in range(len(queue)):
                row, col, dist = queue.popleft()

                for dr, dc in directions:
                    new_r = dr + row
                    new_c = dc + col

                    if isValid(new_r, new_c):
                        grid[new_r][new_c] = dist + 1
                        queue.append((new_r,new_c, dist + 1))
                        seen.add((new_r, new_c))


        

        