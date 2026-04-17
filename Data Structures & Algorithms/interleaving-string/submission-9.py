class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, p = len(s1), len(s2), len(s3)
        if n + m != p:
            return False
        cur = [0] * (m + 1)
        prev = [0] * (m + 1)
        cur[-1] = 1
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i < n and s1[i] == s3[i + j]:
                    cur[j] = prev[j]
                if j < m and s2[j] == s3[i + j]:
                    cur[j] = cur[j + 1]  # = is correct, not |=
            prev = cur
            cur = [0] * (m + 1)
        return prev[0] == 1