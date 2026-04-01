import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(t) > len(t):
            return res
        minLen = 2e9

        countT, countS = defaultdict(int), defaultdict(int)

        for c in t:
            countT[c] += 1
        
        have = 0
        need = len(countT)

        l = 0
        for r in range(len(s)):
            if s[r] in countT:
                countS[s[r]] += 1

                if countT[s[r]] ==countS[s[r]]:
                    have += 1
            
            while have == need:
                if (r - l + 1) < minLen:
                    minLen = (r - l + 1)
                    res = s[l:r + 1]
                
                if s[l] in countT:
                    countS[s[l]] -= 1

                    if countS[s[l]] < countT[s[l]]:
                        have -= 1
                
                l += 1
            
        return res
