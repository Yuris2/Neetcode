class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        counter = {}
        l = 0 
        
        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r],0)

            if r - l + 1 > k + max(counter.values()):
                counter[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res


        