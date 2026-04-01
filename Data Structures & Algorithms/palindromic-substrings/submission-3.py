class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.isPalindrome(s,i,i)
            res += self.isPalindrome(s,i,i+1)
        return res
    
    def isPalindrome(self,s,l,r):
        count = 0
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                return count
            
            count += 1
            l -= 1
            r += 1
        return count
        