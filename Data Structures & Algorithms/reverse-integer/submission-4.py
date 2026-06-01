class Solution:
    def reverse(self, x: int) -> int:
        #Pattern: 
            #Integer manipulation:
                
        #Main idea
            #Extract last digit with %, shift with //
            #If out of bounds, return 0
        lower = -(2 ** 31)
        upper = (2**31) - 1
        isNeg = x < 0
        x = abs(x)
        res = 0

        while x != 0:
            res *= 10
            digit = x % 10
            res += digit
            x = x // 10

            if res < lower or res > upper:
                return 0
        
        if isNeg:
            res = res * -1
        
        return res
        


        