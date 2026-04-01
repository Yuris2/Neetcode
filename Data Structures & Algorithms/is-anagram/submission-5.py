class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 
        letterCounter = {}

        for c in s:
            if c not in letterCounter and c != " ":
                letterCounter[c] = 1
            else:
                letterCounter[c] += 1
        
        for c in t:
            if c in letterCounter and letterCounter[c] > 0:
                letterCounter[c] -= 1
            else:
                return False
        
        return True
        