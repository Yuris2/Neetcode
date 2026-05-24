class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeft, maxLeft = 0,0

        for c in s:
            if c == '(':
                minLeft += 1
                maxLeft += 1
            elif c == ')':
                minLeft -= 1
                maxLeft -= 1
            else:
                minLeft -= 1
                maxLeft += 1
            minLeft = max(0, minLeft)

            if maxLeft < 0:
                return False
        
        return minLeft == 0
        