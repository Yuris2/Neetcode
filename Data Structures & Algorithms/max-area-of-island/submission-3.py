class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])

        seen = set()
        def dfs(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return 0
            elif grid[r][c] != 1 or (r,c) in seen:
                return 0
            
            seen.add((r,c))

            return 1 + (
               dfs(r+1,c) + dfs(r,c+1) + dfs(r-1,c) + dfs(r,c-1) 
            )

        #Creating a dfs area to calculate the area of a given island
        res = 0
        #Iterating through the array
        for r in range(R):
            for c in range(C):
            #If land is seen and not attached to prevIsland
                if grid[r][c] == 1 and (r,c) not in seen:
                    res = max(res, dfs(r,c))
                #Compare area with maxArea
        return res
        #Return maxArea
        