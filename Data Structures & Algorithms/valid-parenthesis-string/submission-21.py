class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for i,c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == '*':
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        while left:
            if star and star[-1] > left[-1]:
                star.pop()
                left.pop()
            else:
                return False
        
        return True

            
        