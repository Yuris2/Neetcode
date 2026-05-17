class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visit, q = set(), deque()


        def bfs(r, c):
            visit.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    R, C = row + dr, col + dc
                    if (R >= 0 and C >= 0 and
                    R < rows and C < cols and
                    grid[R][C] == "1" and (R, C) not in visit):
                        visit.add((R, C))
                        q.append((R, C))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands
        

        