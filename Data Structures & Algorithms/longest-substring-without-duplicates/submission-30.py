class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while r > 0 and s[r] in seen:
                seen.remove(s[l])
                l += 1
            length = r - l + 1
            res = max(res, length)
            seen.add(s[r])
        
        return res

        
        

