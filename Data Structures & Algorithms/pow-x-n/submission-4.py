class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif x == 0:
            return 0
        elif n == 1:
            return x
        
        isNegative = n < 0
        isOdd = (n % 2 == 1)

        res = self.myPow(x, abs(n) // 2)
        res = res * res

        if isOdd:
            res *= x
        if isNegative:
            res = (1 / res)
        
        return res


        