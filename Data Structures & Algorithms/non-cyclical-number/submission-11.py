class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.sumSquare(n)
        fast = self.sumSquare(slow)

        while slow != fast:
            slow = self.sumSquare(slow)
            fast = self.sumSquare(self.sumSquare(fast))
        
        return True if slow == 1 else False
    
    def sumSquare(self, n):
        res = 0
        while n != 0:
            dig = n % 10
            res += (dig * dig)
            n //= 10
        return res
        