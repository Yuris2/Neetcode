class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeft, maxRight = 0,0

        for i, c in enumerate(s):
            if c == '(':
                minLeft += 1
                maxRight += 1
            elif c == ')':
                minLeft -= 1
                maxRight -= 1
            else:
                minLeft -= 1
                maxRight += 1
            
            minLeft = max(0, minLeft)
            if maxRight < 0:
                return False
        
        return minLeft == 0
        