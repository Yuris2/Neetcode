class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        path = []
        #Map every digit to a list of numbers
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
        #I want to run backtracking on the given digits
            #Do we want to use this letter
            #Do we not want to use this letter
        # "23"
        # [ad,ae, af bd,be,bf c]
        #
        def back(i):
            if i >= len(digits):
                if len(path) > 0:
                    res.append("".join(path))
                return
            
            digit = digits[i]
            for ch in mapping[digit]:
                #Include character into our path
                path.append(ch)
                #Commit to this
                back(i + 1)
                #Ok lets try the other characters
                path.pop()
            return
        
        back(0)
        return res


        
        