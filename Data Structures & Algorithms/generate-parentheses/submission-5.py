class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(cntOpen, cntClose):
            if cntOpen == cntClose == n:
                res.append("".join(stack))
                return
            #Two options at each level

            if cntOpen < n:
                stack.append('(')
                backtrack(cntOpen + 1, cntClose)
                stack.pop()
            if cntClose < cntOpen:
                stack.append(')')
                backtrack(cntOpen, cntClose + 1)
                stack.pop()
            
            return

        backtrack(0,0)
        return res
        