class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            #Look for closing  bracket
            if c != "]":
                stack.append(c)
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                #When we find the opening, discard character
                stack.pop()
                #While character is a digit, generate a num to mult
                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                #multiply and append to the stack
                stack.append(int(digit) * substr)
        

        return "".join(stack)

        