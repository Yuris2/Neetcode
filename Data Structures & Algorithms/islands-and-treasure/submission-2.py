import collections

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R,C = len(grid), len(grid[0]) 
        queue = deque()
        seen = set()

        def isValid(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return False
            if grid[r][c] < 0 or (r,c) in seen:
                return False
            return True
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    seen.add((r,c))
        
        steps = 0
        directions = [[1,0],[0,1], [-1,0], [0,-1]]
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = steps

                for dr, dc in directions:
                    new_r = dr + r
                    new_c = dc + c

                    if isValid(new_r, new_c):
                        queue.append((new_r, new_c))
                        seen.add((new_r, new_c))
            steps += 1



        