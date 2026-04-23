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
            if r < 0 or c < 0 or r >= R or c >= C:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            
            res = 1

            for dr, dc in directions:
                new_r, new_c = dr + r, dc + c

                if isValid(new_r, new_c, matrix[r][c]):
                    res = max(res, 1 + dp(new_r, new_c)) 

            cache[(r,c)] = res
            return res

        ans = 0
        for r in range(R):
            for c in range(C):
                if (r,c) not in cache:
                    ans = max(ans, dp(r,c))
        return ans            

        