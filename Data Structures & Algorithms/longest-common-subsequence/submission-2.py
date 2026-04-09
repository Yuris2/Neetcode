class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #Given two strings, return the length of the longest subsequence
        #Return 0 if there are none
        n,m = len(text1), len(text2)
        #i
        curRow = [0] * (m + 1)
        #i + 1
        prevRow = [0] * (m + 1)
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    curRow[j] = 1 + prevRow[j + 1]
                else:
                    curRow[j] = max(prevRow[j], curRow[j + 1])

            prevRow = curRow
            curRow = [0] * (m + 1)
        
        return prevRow[0]