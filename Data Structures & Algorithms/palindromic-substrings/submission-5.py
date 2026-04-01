class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.countPalindromes(s,i,i)
            res += self.countPalindromes(s,i,i+1)
        return res
    
    def countPalindromes(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                return count
            
            l -= 1
            r += 1

            count += 1
        
        return count
                
        