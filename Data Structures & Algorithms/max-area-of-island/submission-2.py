class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])

        seen = set()
        def dfs(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return 0
            elif (r,c) in seen or grid[r][c] != 1:
                return 0
            
            seen.add((r,c))
            
            res = 1 + (dfs(r - 1,c) + 
                dfs(r + 1,c) + 
                dfs(r,c - 1) + 
                dfs(r,c + 1))
            
            return res
        
        maxArea = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and (r,c) not in seen:
                    maxArea = max(maxArea, dfs(r,c))
        
        return maxArea

            