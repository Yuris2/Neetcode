class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1 or x == 0:
            return x
        if n == 0 or x == 1:
            return 1
        
        isNegative = n < 0
        isOdd = (n % 2 == 1)
        
        if isNegative:
            n *= -1
        
        res = self.myPow(x, n // 2)
        ans = res * res

        if isOdd:
            ans *= x
        if isNegative:
            ans = (1 / ans)
        
        return ans
        

        
        
    
        