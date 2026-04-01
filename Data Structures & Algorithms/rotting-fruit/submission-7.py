import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        q = deque()
        seen = set()

        fruit = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    seen.add((r,c))
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fruit += 1

        def isValid(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return False
            if (r,c) in seen or grid[r][c] != 1:
                return False  
            return True

        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        time = 0

        while q and fruit > 0:
            time += 1

            for _ in range(len(q)):
                r,c = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c

                    if isValid(nr, nc):
                        fruit -= 1
                        seen.add((nr,nc))
                        q.append((nr, nc))
        
        if fruit == 0:
            return time
        return -1


            
