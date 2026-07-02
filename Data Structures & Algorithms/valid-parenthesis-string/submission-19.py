class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeft = 0
        maxLeft = 0

        for c in s:
            if c == '(':
                maxLeft += 1
                minLeft += 1
            elif c == ')':
                maxLeft -= 1
                minLeft -= 1
            else:
                maxLeft += 1
                minLeft -= 1

            minLeft = max(minLeft,0)

            if maxLeft < 0:
                return False
        
        return minLeft == 0
        