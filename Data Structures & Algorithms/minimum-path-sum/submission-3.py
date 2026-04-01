class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R,C = len(grid), len(grid[0])
        cache = {}

        def backtrack(r,c):
            #Out of the grid
            if r < 0 or c < 0 or r >= R or c >= C:
                return 2e9
            #Goal
            if r == R - 1 and c == C - 1:
                return grid[r][c]
            if (r,c) in cache:
                return cache[(r,c)]

            #We have two choices
            #down
            choice1 = backtrack(r + 1,c)
            #right
            choice2 = backtrack(r, c + 1)
            #We want to minimize the choices
            cache[(r,c)] = grid[r][c] + min(choice1, choice2)
            return cache[(r,c)] 
        
        return backtrack(0,0)
        