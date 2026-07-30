class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m,p = len(s1), len(s2), len(s3)
        cache = {}

        if n + m != p:
            return False
        
        def dp(i,j):
            if i + j == p:
                return True
            if (i,j) in cache:
                return cache[(i,j)]
            
            res = False

            if i < n and s1[i] == s3[i + j]:
                res = dp(i + 1,j)
            if j < m and s2[j] == s3[i + j]:
                res |= dp(i, j + 1)
            
            cache[(i,j)] = res
            return res
        
        return dp(0,0)
        