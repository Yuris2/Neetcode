class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Approach
        #1. Loop through every character in tokens
        #2. If tokens, is not an operator, add to a stack
        #2. If toeksn is an operator, pop 2 values from stack,
        #   conduct operation, and add result to stack
        #   BE CAREFUL ABOUT DIVISION
        #3. At the end, the stack should contain the final result

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
                a,b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))

        return stack[0]
        