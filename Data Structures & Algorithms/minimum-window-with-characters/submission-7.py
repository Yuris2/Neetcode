class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(s) < len(t):
            return res
        minLen = 2e9

        countT = {}
        countS = {}

        for c in t:
            countT[c] = 1 + countT.get(c,0)
        
        have = 0
        need = len(countT)

        l = 0 
        for r in range(len(s)):
            ch = s[r]
            if ch in countT:
                countS[ch] = 1 + countS.get(ch,0)

                if countS[ch] == countT[ch]:
                    have += 1
                
            while have == need:
                if (r - l + 1) < minLen:
                    res = s[l:r+1]
                    minLen = (r - l + 1)
                
                c = s[l]
                l += 1

                if c in countS:
                    countS[c] -= 1

                    if countS[c] < countT[c]:
                        have -= 1
            
            r += 1
        
        return res
                
        