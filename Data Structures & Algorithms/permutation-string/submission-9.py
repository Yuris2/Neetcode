class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        ord1 = [0] * 26
        ord2 = [0] * 26

        for i in range(len(s1)):
            ord1[ord(s1[i]) - ord('a')] += 1
            ord2[ord(s2[i]) - ord('a')] += 1
        
        if ord1 == ord2:
            return True
        
        for j in range(1, len(s2) - len(s1) + 1):
            ord2[ord(s2[j - 1]) - ord('a')] -= 1
            ord2[ord(s2[j + len(s1) - 1])  - ord('a')] += 1

            if ord2 == ord1:
                return True
        
        return False

        