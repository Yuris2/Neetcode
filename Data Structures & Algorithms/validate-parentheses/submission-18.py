class Solution:
    def isValid(self, s: str) -> bool:
        char_stack = []
        for char in s:
            if char in ["(", "[", "{"]:
                char_stack.append(char)
            elif char == ")": 
                if not char_stack or char_stack[-1] != "(":
                    return False
                else:
                    char_stack.pop()
            elif char == "}":
                if not char_stack or char_stack[-1] != "{":
                    return False
                else:
                    char_stack.pop()
            elif char == "]":
                if not char_stack or char_stack[-1] != "[":
                    return False
                else:
                    char_stack.pop()
            
        
        return len(char_stack) == 0


                        
        