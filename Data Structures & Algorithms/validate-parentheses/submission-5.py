class Solution:
    def isValid(self, s):
        validOpening = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        stack = []

        for c in s:
            if c not in validOpening:
                stack.append(c)
            else:
                if stack and validOpening[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False
        