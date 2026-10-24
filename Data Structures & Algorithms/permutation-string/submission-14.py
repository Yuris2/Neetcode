import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        countS = [0] * 26
        countW = [0] * 26

        for i in range(len(s1)):
            countS[ord(s1[i]) - ord('a')] += 1
            countW[ord(s2[i]) - ord('a')] += 1
        
        if countS == countW:
            return True
        
        for i in range(len(s2) - len(s1)):
            countW[ord(s2[i]) - ord('a')] -= 1
            countW[ord(s2[i + len(s1)]) - ord('a')] += 1

            if countW == countS:
                return True
        
        return False





        