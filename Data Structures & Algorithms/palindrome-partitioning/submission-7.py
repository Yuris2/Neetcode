class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        stack = []

        def back(i):
            if i >= len(s):
                res.append(stack.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j + 1]):
                    stack.append(s[i:j+1])
                    back(j + 1)
                    stack.pop()
        
        back(0)
        return res
    
    def isPalindrome(self,s):
        l,r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True

        