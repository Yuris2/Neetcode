import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1 
                if grid[r][c] == 2:
                    q.append((r, c))
                
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def isValid(r, c):
            if (r < rows and c < cols and r >= 0 and c >= 0 and
            grid[r][c] == 1):
                return True
            return False

        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if isValid(nr, nc):
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            time += 1
        
        return time if fresh == 0 else -1


