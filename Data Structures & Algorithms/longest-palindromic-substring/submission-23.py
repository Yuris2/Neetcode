class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.isPalindrome = ""
        self.maxLen = 0

        def palindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > self.maxLen:
                    self.maxLen = (r - l + 1)
                    self.isPalindrome = s[l:r+1]
                
                l -= 1
                r += 1

        for i in range(len(s)):
            palindrome(i,i)
            palindrome(i,i+1)
        
        return self.isPalindrome
        