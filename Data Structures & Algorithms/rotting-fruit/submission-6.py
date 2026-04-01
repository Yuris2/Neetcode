import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        seen = set()
        queue = deque()
        fruit = 0

        def isValid(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return False
            if grid[r][c] != 1 or (r,c) in seen:
                return False
            return True

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    seen.add((r,c))
                if grid[r][c] == 1:
                    fruit += 1
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        time = 0
        while queue and fruit > 0:

            for i in range(len(queue)):
                row,col = queue.popleft()

                for dr, dc in directions:
                    new_r = row + dr
                    new_c = col + dc

                    if isValid(new_r, new_c):
                        fruit -= 1
                        queue.append((new_r, new_c))
                        seen.add((new_r, new_c))
            time += 1
        
        if fruit == 0:
            return time
        else:
            return -1



        
        