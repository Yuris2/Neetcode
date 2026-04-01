class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []
        #[abbbabbbabbb,c]
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                substr = ""
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                
                #We hit the '['
                stack.pop()
                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit 
                
                stack.append(int(digit)*substr)
        
        return "".join(stack)

        