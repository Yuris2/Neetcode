class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        stack = []

        mapping = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['o','n','m'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        def backtrack(i):
            if i >= len(digits):
                if len(stack) >= 1:
                    res.append("".join(stack))
                return
            
            digit = digits[i]

            for ch in mapping[digit]:
                stack.append(ch)
                backtrack(i + 1)
                stack.pop()
            
            return
        
        backtrack(0)
        return res
        