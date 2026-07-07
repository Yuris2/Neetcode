class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m = len(s1), len(s2)
        cache = {}

        if n + m != len(s3):
            return False
        
        def dp(i,j):
            if i + j == len(s3):
                return True
            if i >= n and j >= m:
                return False
            if (i,j) in cache:
                return cache[(i,j)]
            
            res = False
            if i < n and s1[i] == s3[i + j]:
                res =  dp(i + 1,j)
            if j < m and s2[j]== s3[i + j]: 
                res =  dp(i, j + 1)
            
            cache[(i,j)] = res
            return res
            
        return dp(0,0)
        