class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        
        isNegative = (n < 0)
        isEven = (n % 2 == 0)

        if isNegative:
            n = abs(n)

        # x ^ (n // 2)
        half = self.myPow(x, n // 2)
        res = half * half

        if not isEven:
            res *= x
        
        if isNegative:
            res = (1 / res)
        
        return res

        