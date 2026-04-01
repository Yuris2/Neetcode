class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        ROWS = len(grid)
        COL = len(grid[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COL or grid[r][c] == '#' or grid[r][c] != word[i]:
                return False
            
            grid[r][c] = '#'
            res = (dfs(r + 1,c, i + 1) or
                dfs(r - 1,c, i + 1) or
                dfs(r,c + 1, i + 1) or
                dfs(r,c - 1, i + 1)
            )
            grid[r][c] = word[i]
            return res
        
        for r in range(ROWS):
            for c in range(COL):
                if dfs(r, c , 0):
                    return True
        
        return False
        