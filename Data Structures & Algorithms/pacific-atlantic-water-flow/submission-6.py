class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R,C = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r,c,prevHeight, ocean):
            if r < 0 or c < 0 or r >= R or c >= C:
                return
            if heights[r][c] < prevHeight or (r,c) in ocean:
                return 
            
            ocean.add((r,c))

            dfs(r+1,c, heights[r][c], ocean)
            dfs(r-1,c, heights[r][c], ocean)
            dfs(r,c+1, heights[r][c], ocean)
            dfs(r,c-1, heights[r][c], ocean)

            return
        
        for r in range(R):
            dfs(r,0, 0, pacific)
            dfs(r, C - 1, 0, atlantic)
        
        for c in range(C):
            dfs(0,c,0,pacific)
            dfs(R - 1, c, 0, atlantic)

        res = []
        for r in range(R):
            for c in range(C):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res
        