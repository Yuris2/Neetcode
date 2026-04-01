class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        subLen = len(s1)
        if len(s1) > len(s2):
            return False
        
        n1 = [0] * 26
        n2 = [0] * 26

        for i in range(subLen):
            n1[ord(s1[i]) - ord('a')] += 1
            n2[ord(s2[i]) - ord('a')] += 1
        
        if n1 == n2:
            return True
        
        for i in range(len(s1), len(s2)):
            n2[ord(s2[i]) - ord('a')] += 1
            n2[ord(s2[i - subLen]) - ord('a')] -= 1

            if n1 == n2:
                return True
        
        return False


        