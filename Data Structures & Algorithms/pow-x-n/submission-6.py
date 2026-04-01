class Solution:
    def myPow(self, x: float, n: int) -> float:
        #Divide and conquer approach
        if n == 0:
            return 1
        if x == 0 or x == 1:
            return x
        if n == 1:
            return x
        
        isNegative = n < 0
        if isNegative:
            n *= -1
        
        #Dividing exponent into 2
        res = self.myPow(x, n // 2)
        res *= res

        if n % 2 == 1:
            res *= x
        
        return (1 / res) if isNegative else res


        