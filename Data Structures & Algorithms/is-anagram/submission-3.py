class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        letterCounter = {}

        s = s.replace(" ", "").lower()
        t = t.replace(" ", "").lower()

        if len(s) != len(t):
            return False

        for c in s:
            letterCounter[c] = 1 + letterCounter.get(c,0)
        
        for c in t:
            if c in letterCounter and letterCounter[c] > 0:
                letterCounter[c] -= 1
            else:
                return False
        

        return True

        
        