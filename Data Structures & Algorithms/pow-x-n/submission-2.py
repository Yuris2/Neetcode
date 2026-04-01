class Solution:
    def myPow(self, x: float, n: int) -> float:
        isNegative = False
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            n *= -1
            isNegative = True
        
        #Divide and conquer
        res = self.myPow(x, n // 2)
        res = res * res

        if n % 2 == 1:
            res *= x
        
        if isNegative:
            res = 1 / res
        
        return res
            

        