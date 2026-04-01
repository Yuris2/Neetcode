class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        #Approach
        #-  Since the stack is essentially a global var, have to remove after we put it
        #1. Base Case is if the number of open = close = n
        #2. If the number of open < number of close => Add Open
        #2. If the number of close < number of open => Add Close
        #3. Join string
        def backtrack(countOpen, countClose):
            if countOpen == countClose == n:
                res.append("".join(stack))
                return


            if countOpen < n:
                stack.append("(")
                backtrack(countOpen + 1, countClose)
                stack.pop()
            
            if countClose < countOpen:
                stack.append(")")
                backtrack(countOpen, countClose + 1)
                stack.pop()

        backtrack(0,0)
        return res