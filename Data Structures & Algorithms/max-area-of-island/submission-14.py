class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0
        visit = set()

        def bfs(r, c):
            curArea = 0
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            while q:
                r, c = q.popleft()
                curArea += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr >= 0 and nc >= 0 and
                    nr < rows and nc < cols and 
                    grid[nr][nc] == 1 and 
                    (nr, nc) not in visit):
                        visit.add((nr, nc))
                        q.append((nr, nc))
            return curArea

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = max(area, bfs(r, c))

        return area


