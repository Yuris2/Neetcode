class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                #int drops the decimal so it truncates to 0
                stack.append(int(b / a))

            #If it is a number
            else:
                stack.append(int(c))
        
        return stack[0]

            
        