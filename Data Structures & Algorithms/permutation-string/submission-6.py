class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s1), len(s2)

        if n > m:
            return False
        
        ord1 = [0] * 26
        ord2 = [0] * 26

        for i in range(n):
            ord1[ord(s1[i]) - ord('a')] += 1
            ord2[ord(s2[i]) - ord('a')] += 1
        
        if ord1 == ord2:
            return True
        
        #abc, dabc
        for i in range(n, m):
            ord2[ord(s2[i]) - ord('a')] += 1
            ord2[ord(s2[i - n]) - ord('a')] -= 1

            if ord2 == ord1:
                return True
        
        return False


        