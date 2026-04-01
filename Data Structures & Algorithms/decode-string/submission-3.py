class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                substr = ""

                while stack[-1] != '[':
                    substr = stack.pop() + substr
                
                stack.pop()

                dig = ""
                while stack and stack[-1].isdigit():
                    dig = stack.pop() + dig
                
                stack.append(int(dig) * substr)
        
        return "".join(stack)
        