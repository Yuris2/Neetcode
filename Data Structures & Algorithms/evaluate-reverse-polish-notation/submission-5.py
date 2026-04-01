

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        #Stack is going to be ints
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
                #Floating point division and round towards zero
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        
        return stack[0]
            
        