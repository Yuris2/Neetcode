class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R,C = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        #Water can flow in four directions
        #with height equal to or lower
        #currentHeight >= prevHeight
        def dfs(r,c, prevHeight, ocean):
            if r < 0 or c < 0 or r >= R or c >= C:
                return
            if (r,c) in ocean or heights[r][c] < prevHeight:
                return
            
            ocean.add((r,c))

            dfs(r+1,c,heights[r][c], ocean)
            dfs(r,c+1,heights[r][c], ocean)
            dfs(r-1,c,heights[r][c], ocean)
            dfs(r,c-1,heights[r][c], ocean)
        
        for r in range(R):
            for c in range(C):
                if r == 0 or c == 0:
                    dfs(r,c,0,pacific)
                if r == R - 1 or c == C - 1:
                    dfs(r,c,0,atlantic)
        
        res = []
        for r in range(R):
            for c in range(C):
                if (r,c) in atlantic and (r,c) in pacific:
                    res.append((r,c))
        
        return res


        