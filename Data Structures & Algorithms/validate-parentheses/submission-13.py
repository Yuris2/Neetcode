class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        stack = []

        for c in s:
            if c not in charMap:
                stack.append(c)
            else:
                if stack and stack[-1] == charMap[c]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
        