class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1 or n == 1:
            return x
        if n == 0:
            return 1

        isNegative = n < 0
        isOdd = (n % 2 == 1)
        n = abs(n)

        root = self.myPow(x, n // 2)
        root = root * root

        if isOdd:
            root *= x
        if isNegative:
            root = (1 / root)
        
        return root
        