class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = {}
        mag_dict = {}

        for char in ransomNote:
            if char in ransom_dict:
                ransom_dict[char] += 1
            else:
                ransom_dict[char] = 1
        
        for char in magazine:
            if char in mag_dict:
                mag_dict[char] += 1
            else:
                mag_dict[char] = 1

        for char in ransom_dict:
            if char not in mag_dict:
                return False
            elif ransom_dict[char] > mag_dict[char]:
                return False
        
        return True