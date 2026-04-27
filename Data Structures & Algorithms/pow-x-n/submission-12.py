class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1 or n == 1:
            return x
        if n == 0:
            return 1
        
        isNegative = n < 0
        isOdd =( n % 2 == 1)
        n = abs(n)

        res = self.myPow(x, n // 2)
        res *= res

        if isOdd:
            res *= x
        if isNegative:
            res = (1/res)
        
        return res

        