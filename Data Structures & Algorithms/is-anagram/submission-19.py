class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ordS = [0] * 26
        ordT = [0] * 26

        for i in range(len(s)):
            letterS = ord(s[i]) - ord('a')
            letterT = ord(t[i]) - ord('a')

            ordS[letterS] += 1
            ordT[letterT] += 1
        
        return ordS == ordT
        

    