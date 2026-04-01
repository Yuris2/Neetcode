class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0,0

        for c in s:
            if c == '(':
                leftMin += 1
                leftMax += 1
            elif c == ')':
                leftMin -= 1
                leftMax -= 1
            else:
                #Treat * as a )
                leftMin -= 1
                #Treat * as a (
                leftMax += 1

            #Not enough (
            if leftMax < 0:
                return False
            #Reset
            if leftMin < 0:
                leftMin = 0
        
        return leftMin == 0

        
        