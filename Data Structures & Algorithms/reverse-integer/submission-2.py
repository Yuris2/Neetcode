class Solution:
    def reverse(self, x: int) -> int:
        lower, upper = (-2) ** 31, (2 ** 31) - 1
        isNegative = x < 0
        x = abs(x)

        res = 0

        while x != 0:       
            dig = x % 10
            res = (res * 10) + dig
            x //= 10
        
        if isNegative:
            res *= -1
        if res < lower or res > upper:
            return 0
        
        return res

        