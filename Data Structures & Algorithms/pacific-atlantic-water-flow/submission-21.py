class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R,C = len(heights), len(heights[0])

        pac, atl = set(), set()

        def dfs(r,c,ocean,prev):
            if r < 0 or c < 0 or r >= R or c >= C:
                return
            if(r,c) in ocean or heights[r][c] < prev:
                return
            
            ocean.add((r,c))

            dfs(r+1,c,ocean, heights[r][c])
            dfs(r,c+1,ocean, heights[r][c])
            dfs(r-1,c,ocean, heights[r][c])
            dfs(r,c-1,ocean, heights[r][c])

        for r in range(R):
            for c in range(C):
                if r == 0 or c == 0:
                    dfs(r,c,pac,0)
                if r == R - 1 or c == C - 1:
                    dfs(r,c,atl,0)
        
        res = []
        for r,c in pac:
            if (r,c) in atl:
                res.append((r,c))
        return res
            

        