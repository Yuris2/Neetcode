class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0,0

        for c in s:
            if c == '(':
                leftMax += 1
                leftMin += 1
            elif c == ')':
                leftMax -= 1
                leftMin -= 1
            else:
                leftMax += 1
                leftMin -= 1
            
            #Don't have enough matches of left
            if leftMax < 0:
                return False
            leftMin = max(0, leftMin)
        
        return leftMin == 0
        