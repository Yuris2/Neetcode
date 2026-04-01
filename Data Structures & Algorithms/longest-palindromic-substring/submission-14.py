class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxLength = 0
        self.res = ""

        def palindrome(l,r):
            while r < len(s) and l >=0 and s[l] == s[r]:
                if (r - l + 1) > self.maxLength:
                    self.maxLength = (r - l + 1)
                    self.res = s[l:r + 1]
                l -= 1
                r += 1
        
        for i in range(len(s)):
            palindrome(i,i)
            palindrome(i,i+1)
        
        return self.res
                
        


        