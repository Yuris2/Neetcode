class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 1:
            return 1
        if n == 1:
            return x
        
        isNegative = n < 0
        n = abs(n)
        #To power of n (x^4 = x^2 * x^2)
        res = self.myPow(x, n // 2)
        res = res * res

        if n % 2 == 1:
            res *= x
        if isNegative:
            res = (1 / res)
        
        return res


        