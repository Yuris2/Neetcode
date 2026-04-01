class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        l = 0
        res = 0

        for r in range(len(s)):
            #Count char and occurence
            counter[s[r]] = 1 + counter.get(s[r],0)

            #Window condition
            #with the max occ, if the max occ + k is smaller than length of window
            #can't be the longest repeating character so have to adjust the window
            while (max(counter.values()) + k) < (r - l + 1):
                counter[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))

        return res            
            


        