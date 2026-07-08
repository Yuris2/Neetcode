class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.max = 0
        self.res = ""

        def isPalindrome(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > self.max:
                    self.max = r - l + 1
                    self.res = s[l:r + 1]
                l -= 1
                r += 1
        
        for i in range(len(s)):
            isPalindrome(i,i+1)
            isPalindrome(i,i)
        
        return self.res

        
        