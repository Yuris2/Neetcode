class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R,C = len(heights), len(heights[0])
        res = []

        def dfs(r,c, prevHeight, seen):
            if r < 0 or c < 0 or r >= R or c >= C:
                return
            elif (r,c) in seen or heights[r][c] < prevHeight:
                return
            
            seen.add((r,c))

            dfs(r+1,c, heights[r][c], seen)
            dfs(r,c+1, heights[r][c], seen)
            dfs(r-1,c, heights[r][c], seen)
            dfs(r,c-1, heights[r][c], seen)

            return
        
        pacific = set()
        atlantic = set()

        for r in range(R):
            dfs(r,0,0,pacific)
            dfs(r,C - 1,0,atlantic)
        
        for c in range(C):
            dfs(0,c, 0, pacific)
            dfs(R -1, c, 0, atlantic)
        
        for r in range(R):
            for c in range(C):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        
        return res
            

        