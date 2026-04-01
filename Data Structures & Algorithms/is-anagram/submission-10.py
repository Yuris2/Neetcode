class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counterS = {}

        for c in s:
            counterS[c] = 1 + counterS.get(c,0)
        
        for c in t:
            if c not in counterS or counterS[c] <= 0:
                return False
            else:
                counterS[c] -= 1
        
        return True

    