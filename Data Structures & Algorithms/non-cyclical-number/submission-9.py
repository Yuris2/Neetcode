class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.sumOfSquare(n)
        fast = self.sumOfSquare(slow)

        while slow != fast:
            slow = self.sumOfSquare(slow)
            fast = self.sumOfSquare(self.sumOfSquare(fast))

        if slow == 1:
            return True
        else:
            return False
    
    def sumOfSquare(self, n):
        res = 0

        while n != 0:
            dig = n % 10
            res += (dig ** 2)
            n //= 10
        
        return res
        