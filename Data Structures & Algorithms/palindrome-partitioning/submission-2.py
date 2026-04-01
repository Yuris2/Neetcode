class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        stack = []

        def backtrack(i):
            if i >= len(s):
                res.append(stack.copy())
                return
            
            #Go through every index after i to the end of the string
            for j in range(i, len(s)):
                if self.isPalindrome(s,i,j):
                    #Add palindrome to the stack
                    stack.append(s[i:j + 1])
                    #Go down decision tree
                    backtrack(j + 1)
                    #go down decision tree where you don't include it
                    stack.pop()
        
        backtrack(0)
        return res
    
    def isPalindrome(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
        