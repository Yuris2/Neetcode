class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R,C = len(matrix), len(matrix[0])
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        cache = {}

        def isValid(r,c,prev):
            if r < 0 or c < 0 or r >= R or c >= C:
                return False
            if matrix[r][c] <= prev:
                return False
            return True

        def dp(r,c):
            res = 1
            if (r,c) in cache:
                return cache[(r,c)]
            for dr, dc in directions:
                newR, newC = dr + r, dc + c
                if isValid(newR,newC,matrix[r][c]):
                    res = max(res, 1 +dp(newR,newC))
            
            cache[(r,c)] = res
            return res
        
        res = 0
        for r in range(R):
            for c in range(C):
                res = max(res, dp(r,c))
        return res

        