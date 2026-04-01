class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def back(openC, closeC):
            if openC == closeC == n:
                res.append("".join(stack))
                return
            
            if openC < n:
                stack.append("(")
                back(openC + 1, closeC)
                stack.pop()
            if closeC < openC:
                stack.append(")")
                back(openC , closeC + 1)
                stack.pop()
        
        back(0,0)
        return res
        