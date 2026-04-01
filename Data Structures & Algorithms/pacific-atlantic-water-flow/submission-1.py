class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        res = []

        pacific = set()
        atlantic = set()

        def dfs(r, c, visit, prevHeight):
            if r < 0 or c < 0 or r >= ROW or c >= COL:
                return
            elif (r,c) in visit or heights[r][c] < prevHeight:
                return

            visit.add((r,c))

            dfs(r + 1,c, visit, heights[r][c])        
            dfs(r - 1,c, visit, heights[r][c])   
            dfs(r,c + 1, visit, heights[r][c])   
            dfs(r,c - 1, visit, heights[r][c])

        #Running dfs on the board
        for c in range(COL):
            dfs(0, c, pacific, heights[0][c])   
            dfs(ROW - 1, c, atlantic, heights[ROW - 1][c])   
        
        for r in range(ROW):
            dfs(r, 0, pacific, heights[r][0])   
            dfs(r, COL - 1, atlantic, heights[r][COL - 1])   
        
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
                
        return res

