class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if x == 0:
            return x 
        
        isNegative = n < 0
        isOdd = (n % 2 != 0)
        n = abs(n)

        res = self.myPow(x, n // 2)
        res = res * res

        if isOdd:
            res *= x
        if isNegative:
            res = (1 / res)
        
        return res
        

        

        