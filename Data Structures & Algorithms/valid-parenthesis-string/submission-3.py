class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        wildcard = []

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == '*':
                wildcard.append(i)
            else:
                #Try and get (
                if stack:
                    stack.pop()
                #Use a wildcard
                elif wildcard:
                    wildcard.pop()
                #Nothing available
                else:
                    return False
        
        while stack and wildcard:
            #( appears before a wildcard [*(]
            if stack.pop() > wildcard.pop():
                return False
        
        return len(stack) == 0
        

        
        