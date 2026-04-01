class Solution:
    def reverse(self, x: int) -> int:


        isNegative = x < 0

        if abs(x) < 10:
            return x
        
        if isNegative:
            x *= -1
        
        res = 0

        while x > 0:
            dig = x % 10
            res = (res * 10) + dig
            x = x // 10

        if res > (2**31) - 1 or res < (-2**31):
            return 0
        
        return res if not isNegative else -res
        