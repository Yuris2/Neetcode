class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False
        
        ord1 = [0] * 26
        ord2 = [0] * 26

        for i in range(len(s1)):
            ord1[(ord(s1[i]) - ord('a'))] += 1
            ord2[(ord(s2[i]) - ord('a'))] += 1
        
        if ord1 == ord2:
            return True
        
        for i in range(n, len(s2)):
            ord2[(ord(s2[i]) - ord('a'))] += 1
            ord2[(ord(s2[i - n]) - ord('a'))] -= 1

            if ord1 == ord2:
                return True

        return False