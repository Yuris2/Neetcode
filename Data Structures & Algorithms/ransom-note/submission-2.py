class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        for c in magazine:
            counter[c] = 1 + counter.get(c,0)
        
        for c in ransomNote:
            if c not in counter or counter[c] <= 0:
                return False
            else:
                counter[c] -= 1
        
        return True

        