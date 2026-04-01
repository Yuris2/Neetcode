class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        size = 0
        l, r = 0, 0
        res = 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                size -= 1
                l += 1
            seen.add(s[r])
            size += 1
            res = max(size, res)
            r += 1
        return res