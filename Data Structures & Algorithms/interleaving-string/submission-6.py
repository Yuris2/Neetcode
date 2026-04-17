class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m,p = len(s1), len(s2), len(s3)
        cache = {}
        if n + m != p:
            return False
            
        def dp(i,j):
            #If we can use all characters to form s3
            if i >= n and j >= m:
                return True
            if (i,j) in cache:
                return cache[(i,j)]
            
            c1, c2 = False, False
            if i < n and s1[i] == s3[i + j]:
                c1 = dp(i + 1, j)
            if j < m and s2[j] == s3[i + j]:
                c2 = dp(i, j + 1)
            
            cache[(i,j)] = c1 or c2
            return c1 or c2
        
        return dp(0,0)

        