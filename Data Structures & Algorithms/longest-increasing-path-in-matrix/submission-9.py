class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        cache = [[-1] * C for _ in range(R)]

        def dp(r,c,prev):
            if r < 0 or r >= R or c < 0 or c >= C:
                return 0
            if grid[r][c] <= prev:
                return 0
            if cache[r][c] != -1:
                return cache[r][c]
            
            res = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= R or nc < 0 or nc >= C:
                    continue
                if grid[nr][nc] > grid[r][c]:
                    res = max(res, 1 + dp(nr, nc, grid[r][c]))
            
            cache[r][c] = res
            return res
        
        res = 0
        for r in range(R):
            for c in range(C):
                if cache[r][c] == -1:
                    res = max(res, dp(r,c,-1))
        return res

            


        