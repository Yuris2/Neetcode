class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        ordS = [0] * 26
        ordT = [0] * 26

        for i in range(len(s)):
            ordS[(ord(s[i]) - ord('a'))] += 1
            ordT[(ord(t[i]) - ord('a'))] += 1
        
        return ordS == ordT

        