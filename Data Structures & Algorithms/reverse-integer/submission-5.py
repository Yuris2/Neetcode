class Solution:
    def reverse(self, x: int) -> int:
        lower = -(2**31)
        upper = (2**31) - 1

        isNeg = x < 0
        x = abs(x)

        res = 0

        while x != 0:
            res = res * 10
            digit = x % 10
            res += digit
            x = x // 10
        
        res = -res if isNeg else res

        if res < lower or res > upper:
            return 0
        
        return res 
        