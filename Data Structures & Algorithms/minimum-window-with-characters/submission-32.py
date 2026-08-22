import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        countT = Counter(t)
        countS = defaultdict(int)

        have = 0
        need = len(countT)

        l = 0
        res = ""
        minLen = 2e9

        for r in range(len(s)):
            if s[r] in countT:
                countS[s[r]] += 1

                if countS[s[r]] == countT[s[r]]:
                    have += 1
            
            while have == need:
                if (r - l + 1) < minLen:
                    res = s[l:r+1]
                    minLen = (r - l + 1)

                if s[l] in countT:
                    countS[s[l]] -= 1

                    if countS[s[l]] < countT[s[l]]:
                        have -= 1

                
                l += 1
        
        return res
        