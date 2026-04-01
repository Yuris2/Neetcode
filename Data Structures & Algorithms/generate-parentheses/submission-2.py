class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(openC, closeC):
            if n == openC == closeC:
                #Make the stack a string and add to res
                pair = "".join(stack)
                res.append(pair)
            
            #Case 1: open < n
            if openC < n:
                #add to stack
                stack.append("(")
                #go down that path
                backtrack(openC + 1, closeC)
                #backtrack
                stack.pop()
            #Case 2: if number of close < openC
            if closeC < openC:
                stack.append(")")
                backtrack(openC, closeC + 1)
                stack.pop()
        
        backtrack(0,0)
        return res
        