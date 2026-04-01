class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charMap = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:
            if c not in charMap:
                stack.append(c)
            else:
                if stack and stack[-1] == charMap[c]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        else:
            return True
        