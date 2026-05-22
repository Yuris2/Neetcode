class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charSet = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        for c in s:
            if c not in charSet:
                stack.append(c)
            else:
                if stack and stack[-1] == charSet[c]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
                
        