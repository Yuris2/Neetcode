class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #Pattern
            #Backtrack on the digits with letter combos
        #General Idea
            #Run backtracking on digits using the letter mapping
            #To generate every possibility of letters
        
        res = []
        stack = []

        combinations = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }

        def back(i):
            if i >= len(digits):
                if len(stack) > 0:
                    res.append("".join(stack))
                return
                
            
            for c in combinations[digits[i]]:
                stack.append(c)
                back(i + 1)
                stack.pop()

        back(0)  
        return res      