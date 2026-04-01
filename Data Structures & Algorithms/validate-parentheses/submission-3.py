class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        stack = []
        for c in s:
            #Opening bracket
            if c not in charMap:
                stack.append(c)
            else:
                if stack and charMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        else:
            return True
        