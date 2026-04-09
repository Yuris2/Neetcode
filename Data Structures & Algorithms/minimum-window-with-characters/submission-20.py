import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        minLen = 2e9
        if len(t) > len(s):
            return res
        
        countS, countT = defaultdict(int), Counter(t)

        have = 0
        need = len(countT)

        l = 0
        for r, c in enumerate(s):
            if c in countT:
                countS[c] +=1
                
                if countS[c] == countT[c]:
                    have += 1
            
            while have == need:
                if (r - l + 1) < minLen:
                    res = s[l:r+1]
                    minLen = (r - l + 1)
                
                ch = s[l]
                if ch in countT:
                    countS[ch] -= 1

                    if countS[ch] < countT[ch]:
                        have -= 1
                l += 1
        
        return res


        
        