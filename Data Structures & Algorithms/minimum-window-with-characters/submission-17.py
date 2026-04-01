from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(t) > len(s):
            return res
        
        countS = defaultdict(int)
        countT = defaultdict(int)

        for c in t:
            countT[c] += 1
        
        have, need = 0, len(countT)
        minLen = 2e9
        
        l = 0
        for r in range(len(s)):
            if s[r] in countT:
                countS[s[r]] += 1
                if countS[s[r]] == countT[s[r]]:
                    have += 1
            
            while have == need:
                if (r - l + 1) < minLen:
                    minLen = (r - l + 1)
                    res = s[l:r+1]
                
                if s[l] in countT:
                    countS[s[l]] -= 1

                    if countS[s[l]] < countT[s[l]]:
                        have -= 1
                
                l += 1
        
        return res

            


        