class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        seen = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return 0
            elif grid[r][c] != 1 or (r,c) in seen:
                return 0
            
            seen.add((r,c))

            return 1 + dfs(r,c + 1) + dfs(r,c - 1) + dfs(r + 1,c) + dfs(r - 1,c)
        
        maxArea = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r,c) not in seen:
                    maxArea = max(dfs(r,c), maxArea)
        
        return maxArea

            
        