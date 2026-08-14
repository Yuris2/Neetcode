class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        countT = {} # char -> count (t)
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        need = len(countT) # 3
        
        l, have, minWin = 0, 0, [2e9, 0, 0] # len, l, r
        window = {} # char -> count (windows of s)
        found = False
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1

            # valid window, attempt to shrink
            while have == need:
                found = True
                if (r - l + 1) < minWin[0]:
                    minWin = [r - l + 1, l, r]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
            
                l += 1
            
        return s[minWin[1]:minWin[2] + 1] if found else ""

            
            

                    
                
                
            




                

            
                
