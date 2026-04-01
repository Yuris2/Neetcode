class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Neighbor height has to be equal to or lower
        R,C = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r,c, ocean, prevHeight):
            if r < 0 or c < 0 or r >= R or c >= C:
                return 
            if (r,c) in ocean or heights[r][c] < prevHeight:
                return
            
            ocean.add((r,c))
            dfs(r+1,c,ocean, heights[r][c])
            dfs(r,c+1,ocean, heights[r][c])
            dfs(r-1,c,ocean, heights[r][c])
            dfs(r,c-1,ocean, heights[r][c])
        
        for r in range(R):
            dfs(r,0,pacific, 0)
            dfs(r, C-1, atlantic,0)
        
        for c in range(C):
            dfs(0,c,pacific, 0)
            dfs(R-1, c, atlantic, 0)
        
        res = []
        for r in range(R):
            for c in range(C):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append((r,c))
        return res



        