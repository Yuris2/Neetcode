class Solution:
    def isValid(self, s: str) -> bool:
        #Approach
        #1.     Check if char is a closing/opening tag
        #1a     If opening, add to a stack
        #1b     If closing, check if top of stack is corr correspond open. Pop if true
        #2.     Go back to step 1
        stack = []

        charMap = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }

        #2. 
        for c in s:
            #1. Opening
            if c not in charMap:
                stack.append(c)
            #1b. Closing
            else:
                #if the closing tag occurs before any opening
                #or if the top of stack does not match
                if not stack or charMap[c] != stack[-1] :
                    return False
                else:
                    stack.pop()
        
        return not stack



        