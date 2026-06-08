class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxArea = 0
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            area = 1

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr >= 0 and nc >= 0 and nr < rows and nc < cols and 
                    grid[nr][nc] == 1 and
                    (nr, nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr, nc))
                        area += 1

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxArea = max(maxArea, bfs(r, c))
        
        return maxArea
