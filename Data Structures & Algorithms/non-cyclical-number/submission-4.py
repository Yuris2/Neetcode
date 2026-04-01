class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfDigits(n)

        while slow != fast:
            slow = self.sumOfDigits(slow)
            fast = self.sumOfDigits(self.sumOfDigits(fast))
        
        if slow == 1:
            return True
        else:
            return False
    
    def sumOfDigits(self, n):
        res = 0
        while n != 0:
            digit = n % 10
            res += (digit ** 2)
            n //= 10
        return res

        