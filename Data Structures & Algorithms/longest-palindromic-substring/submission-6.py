class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        self.maxLen = 0

        def palindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > self.maxLen:
                    self.res = s[l:r+1]
                    self.maxLen = (r - l + 1)
                l -= 1
                r += 1
            
            return
        
        for i in range(len(s)):
            palindrome(i, i)
            palindrome(i, i + 1)
        
        return self.res
        