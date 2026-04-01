class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [""]
        maxLen = [0]

        def expansion(s,l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen[0]:
                    maxLen[0] = (r - l) + 1
                    res[0] = s[l:r+1]
                
                l -= 1
                r += 1
        
        for i in range(len(s)):
            expansion(s,i,i)
            expansion(s,i, i + 1)
        
        return res[0]
        