class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False
        
        charS = [0] * 26
        charT = [0] * 26

        for i in range(n):
            charS[ord(s[i]) - ord('a')] += 1
            charT[ord(t[i]) - ord('a')] += 1
        
        return charS == charT
        