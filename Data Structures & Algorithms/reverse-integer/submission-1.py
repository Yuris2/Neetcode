class Solution:
    def reverse(self, x: int) -> int:
        lowerBound, upperBound = (-2) ** 31, (2) ** 31 - 1
        res = 0
        if not (lowerBound < x < upperBound):
            return res
        isNegative = x < 0
        x = abs(x)

        while x != 0:
            digit = x % 10
            res = (res * 10) + digit
            x = x // 10
        
        if isNegative:
            res *= -1

        if not (lowerBound <= res <= upperBound):
            return 0
        
        return res
        