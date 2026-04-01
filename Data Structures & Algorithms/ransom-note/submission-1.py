class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineC = {}
        for c in magazine:
            magazineC[c] = 1 + magazineC.get(c, 0)
        
        for c in ransomNote:
            if c in magazineC and magazineC[c] > 0:
                magazineC[c] -= 1
            else:
                return False
        
        return True
        