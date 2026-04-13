class Solution:
    def reverse(self, x: int) -> int:
        minVal, maxVal = -2**31, 2**31 - 1
        isNeg = x < 0
        x = abs(x)
        res = 0

        while x != 0:
            dig = x % 10
            res = (res * 10) + dig
            x //= 10
        
        if isNeg:
            res *= -1
        
        if res < minVal or res > maxVal:
            return 0
        return res
        