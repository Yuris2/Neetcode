class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
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