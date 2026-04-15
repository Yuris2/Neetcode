class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m,p = len(s1), len(s2), len(s3)

        if n + m != p:
            return False

        cur = [False] * (m + 1)
        prev = [False] * (m + 1)
        cur[-1] = True

        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i < n and s1[i] == s3[i + j] and prev[j]:
                    cur[j] = prev[j]
                if j < m and s2[j] == s3[i + j] and cur[j + 1]:
                    cur[j] = cur[j + 1]
            prev = cur 
            cur = [False] * (m + 1)
        
        return prev[0]
                    


            
            
            
        