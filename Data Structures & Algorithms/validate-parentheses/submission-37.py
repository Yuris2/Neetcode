# for c in s
# if c is a close bracket
# top and bottom of stack are matching pairs in the hashmap
# pop from stack
# else return False because they aren't matching

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')' : '(', ']' : '[', '}' : '{'}
        
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
                    
                