class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if x == 0:
            return 0
        
        isNegative = False if n > 0 else True
        isOdd = True if n % 2 == 1 else False

        res = self.myPow(x, abs(n) // 2)
        res = res * res
        
        if isOdd:
            res *= x
        if isNegative:
            res = (1 / res)
        
        return res
        #Divide and conquer
        