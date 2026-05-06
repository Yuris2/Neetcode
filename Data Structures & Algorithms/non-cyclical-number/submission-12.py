class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.sumOfSquares(n)
        fast = self.sumOfSquares(slow)

        while slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))
        
        return True if slow == 1 else False
    
    def sumOfSquares(self, n):
        res = 0
        while n != 0:
            dig = n % 10
            res += (dig ** 2)
            n = n // 10
        return res
        