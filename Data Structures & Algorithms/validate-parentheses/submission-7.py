class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        validOpen = {
            '}': '{',
            ')': "(",
            ']': "["
        }

        for c in s:
            #If the character is an opening tag
            if c not in validOpen:
                stack.append(c)
            else:
                #If stack has values and top of stack
                #corresponds with the opening of current closing tag
                if stack and stack[-1] == validOpen[c]:
                    stack.pop()
                else:
                    return False
        
        #return if stack is empty
        return not stack
        