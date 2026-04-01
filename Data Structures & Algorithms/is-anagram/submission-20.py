class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        
        for char in t:
            if char not in s_dict:
                return False
            elif s_dict[char] == 0:
                return False
            else:
                s_dict[char] -= 1
        
        return not all(s_dict.values())