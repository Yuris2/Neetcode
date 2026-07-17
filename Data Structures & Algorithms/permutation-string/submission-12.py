class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count1 = {} # {a: 1, b: 1, c: 1}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        

        count2 = {} # {c: 1, a: 1, b: 1}
        l = 0
        for r in range(len(s2)):
            count2[s2[r]] = 1 + count2.get(s2[r], 0)
            while (r - l + 1) > len(s1):
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l += 1
            if count2 == count1:
                return True
        
        return False
            
            


        # if s2 length < s1 length, return False
        # --

        # if ascii vals in a window are the same then True
        # if length and ascii vals are the same

        # ---

        # maintain a hashmap of chars and their counts for the window ->
        # if it matches that of the str return True
        # how to slide window ?
            # s2[l] is in the s1 hashmap


