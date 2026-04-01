class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(t) > len(s):
            return res
        minLen = 2e9

        countT = {}
        countS = {}

        for c in t:
            countT[c] = 1 + countT.get(c,0)

        have, need = 0, len(countT)

        l = 0
        for r in range(len(s)):
            #Add to window
            ch = s[r]
            if ch in countT:
                countS[ch] = 1 + countS.get(ch, 0)
                #If we meet the character condition (we have enough to build window)
                if countS[ch] == countT[ch]:
                    have += 1
            
            #Adjust window
            while have == need:
                #Check if we can update result
                if (r - l + 1) < minLen:
                    minLen = (r - l + 1)
                    res = s[l:r + 1]
                c = s[l]
                #If our character is one we need to include
                if c in countT:
                    #Decrement our window
                    countS[c] -= 1
                    #If we don't have a valid window
                    if countS[c] < countT[c]:
                        have -= 1
                #Keep moving left of window
                l += 1
        
        return res
                    






















        