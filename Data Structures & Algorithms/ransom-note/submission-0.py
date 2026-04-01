class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for c in magazine:
            letters[c] = 1 + letters.get(c,0)
        
        for c in ransomNote:
            if c not in letters or letters[c] == 0:
                return False
            letters[c] -= 1
        
        return True
        