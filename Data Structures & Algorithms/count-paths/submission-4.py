class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #only allowed to move down and right
        cache = {}
        def backtrack(r,c):
            if r < 0 and c < 0 or r >= m or c >= n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1 
            if (r,c) in cache:
                return cache[(r,c)]

            cache[(r,c)] =  backtrack(r + 1,c) + backtrack(r, c + 1)
            
            return cache[(r,c)]
        
        return backtrack(0,0)
        