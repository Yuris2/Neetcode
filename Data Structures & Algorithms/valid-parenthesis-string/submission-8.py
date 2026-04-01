class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        wildcard = []

        #((**)
        #[0,1]
        #[2,3]

        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == '*':
                wildcard.append(i)
            else:
                if left:
                    left.pop()
                elif wildcard:
                    wildcard.pop()
                else:
                    return False
        
        while left and wildcard:
            if left[-1] > wildcard[-1]:
                return False
            left.pop()
            wildcard.pop()
        
        return len(left) == 0
        