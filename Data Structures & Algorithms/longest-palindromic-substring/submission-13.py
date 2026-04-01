class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxLength = 0
        self.res = ""

        def isPalindrome(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1

                if length > self.maxLength:
                    self.res = s[l:r + 1]
                    self.maxLength = length

                l -= 1
                r += 1
        
        for i in range(len(s)):
            isPalindrome(i,i)
            isPalindrome(i,i + 1)
        
        return self.res

    

        