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
        
        #abc

        #dddbca
        for i in range(len(s2) - len(s1)):
            #Remove first char in window
            removeChar = s2[i]
            ord2[ord(removeChar) - ord('a')] -= 1
            #Add char at the end of window
            newChar = s2[i + len(s1)]
            ord2[ord(newChar) - ord('a')] += 1

            if ord1 == ord2:
                return True
        
        return False



        