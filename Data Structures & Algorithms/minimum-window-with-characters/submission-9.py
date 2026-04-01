class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(t) > len(s):
            return res
        minLen = 2e9
        countT, countS = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c,0)
        
        have = 0
        need = len(countT)

        L = 0
        for R in range(len(s)):
            ch = s[R]
            if ch in countT:
                countS[ch] = 1 + countS.get(ch,0)

                if countS[ch] == countT[ch]:
                    have += 1
            
            while have == need:
                if (R - L + 1) < minLen:
                    res = s[L:R+1]
                    minLen = (R - L + 1)
                
                c = s[L]

                if c in countT:
                    countS[c] -= 1
                

                    if countS[c] < countT[c]:
                        have -= 1
                
                L += 1
        
        return res
        