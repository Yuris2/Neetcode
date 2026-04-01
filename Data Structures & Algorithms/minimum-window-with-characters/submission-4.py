class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        minLen = 2e9
        if len(t) > len(s):
            return res 
        
        #T
        countT = {}

        for c in t:
            countT[c] = 1 + countT.get(c,0)
        #Count of the substring
        countS = {}

        have = 0
        need = len(countT)
        l = 0

        for r in range(len(s)):
            if s[r] in countT:
                countS[s[r]] = 1 + countS.get(s[r],0)
                #If we have fulfilled one of the char conditions
                if countS[s[r]] == countT[s[r]]:
                    have += 1
            
            while have == need:
                #If the length of the window can produce a new result
                if (r - l + 1) < minLen:
                    minLen = (r - l + 1)
                    res = s[l:r+1]
                c = s[l]
                
                #If the character at the leftmost is in T
                if c in countT:
                    countS[c] -= 1

                    if countS[c] < countT[c]:
                        have -= 1
                
                l += 1
        
        return res
        