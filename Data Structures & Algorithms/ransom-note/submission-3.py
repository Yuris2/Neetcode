class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans_dict = {}
        mag_dict = {}

        for char in ransomNote:
            if char in rans_dict:
                rans_dict[char] += 1
            else:
                rans_dict[char] = 1
        
        for char in magazine:
            if char in mag_dict:
                mag_dict[char] += 1
            else:
                mag_dict[char] = 1
        
        for char in rans_dict:
            if char not in mag_dict:
                return False
            elif rans_dict[char] > mag_dict[char]:
                return False
        
        return True