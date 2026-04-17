class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R,C = len(matrix), len(matrix[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        cache = {}

        def isVald(r,c, prev):
            if r < 0 or c < 0 or r >= R or c >= C:
                return False
            if matrix[r][c] <= prev:
                return False
            return True

        def dp(r,c):
            if r < 0 or c < 0 or r >= R or c >= C:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            
            res = 1

            for dr, dc in directions:
                nR, nC = dr + r, dc + c

                if isVald(nR, nC, matrix[r][c]):
                    res = max(res, 1 + dp(nR, nC))
            
            cache[(r,c)] = res
            return res
        
        res = 0
        for r in range(R):
            for c in range(C):
                if (r,c) not in cache:
                    res = max(res, dp(r,c))
        return res
                
        