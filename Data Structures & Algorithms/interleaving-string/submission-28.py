class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m = len(s1), len(s2)

        if n + m != len(s3):
            return False
        
        #a      abb
        #ab

        #a
        #aa
        #ab

        cache = [[-1] * (m + 1) for _ in range(n + 1)]
        def dp(i,j):
            if (i + j) == len(s3):
                return True
            if cache[i][j] != -1:
                return cache[i][j]
            
            c1,c2 = False, False

            if i < n and s1[i] == s3[i + j]:
                c1 = dp(i + 1,j)
            if j < m and s2[j] == s3[i + j]:
                c2 = dp(i, j + 1)
            
            cache[i][j] = c1 or c2
            return cache[i][j]
        
        return dp(0,0)
        #Want to break this down into a subproblem
        #Two choices
            #1. If We can try a letter in s1, move to next
                #We want to track letters in s1
            #2. If We can try a letter in s2, move to next
                #We want to track letters in s2

        #We try to create s3 by trying every combination of the choices
        #Continue unti we have reached the end of s3
            #Return True if we can reach end else False



        