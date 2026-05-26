

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        def isValid(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
            grid[r][c] == 0 or grid[r][c] == 2):
                return False
            return True

        
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if isValid(nr, nc):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
            minutes += 1
            
        return minutes if fresh == 0 else -1
        
            


                
            
