class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            visit.add((r, c))
            q.append((r, c))
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    R = r + dr
                    C = c + dc
                    if (R >= 0 and C >= 0 and
                    R < rows and C < cols and
                    (R, C) not in visit and
                    grid[R][C] == "1"):
                        visit.add((R, C))
                        q.append((R, C))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands

