class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        res = 0

        l = 0
        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            while max(counter.values()) + k < (r - l + 1):
                counter[s[l]] -= 1
                l += 1   
            res = max(res, r - l + 1)
        
        return res

        