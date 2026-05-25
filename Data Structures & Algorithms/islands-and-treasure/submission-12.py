class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c, 0))

        def isValid(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
            (r, c) in visit or grid[r][c] == -1):
                return False
            return True
        
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while q:
            r, c, prevDistance = q.popleft()
            distance = 1 + prevDistance
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if isValid(nr, nc):
                    grid[nr][nc] = distance
                    visit.add((nr, nc))
                    q.append((nr, nc, distance))

                    


