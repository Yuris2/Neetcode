class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {'}' :'{',
            ']' : '[',
            ')' : '('}
        
        stack = []

        for c in s:
            if c not in charMap:
                stack.append(c)
            else:
                if stack and charMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        
        return True


        #Iterate Through String
        #Check the current char
            #If the current char is an opening tag
            #Prioritize Looking for its closing tag
            #If the current char check if its opening tag is 
            #prioritzed
                #If not, not valid
        
        #After looking, are there still any values in priority
        #If so, not valid


        