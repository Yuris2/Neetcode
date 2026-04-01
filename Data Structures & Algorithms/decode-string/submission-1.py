class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                
                #throw the bracket away
                stack.pop()
                factor = ""
                while stack and stack[-1].isdigit():
                    factor = stack.pop() + factor

                stack.append(int(factor) * substr)
        
        return "".join(stack)


        