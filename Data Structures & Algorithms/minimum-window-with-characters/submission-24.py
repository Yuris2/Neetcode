import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(s) < len(t):
            return res
        
        minLen = 2e9
        countT = Counter(t)
        countS = defaultdict(int)

        have, need = 0, len(countT)

        l = 0
        for r, c in enumerate(s):
            if c in countT:
                countS[c] += 1

                if countS[c] == countT[c]:
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
