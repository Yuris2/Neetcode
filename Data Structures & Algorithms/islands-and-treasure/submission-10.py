class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def isValid(r, c):
            if r < 0 or c < 0 or r == rows or c == cols:
                return False
            if grid[r][c] == -1 or (r, c) in visit:
                return False
            return True
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    q.append((r, c, 0))

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while q:
            r, c, prevDistance = q.popleft()
            distance = prevDistance + 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if isValid(nr, nc):
                    grid[nr][nc] = distance
                    visit.add((nr, nc))
                    q.append((nr, nc, distance))
        

