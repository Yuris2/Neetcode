class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.sumOfDigits(n)
        fast = self.sumOfDigits(slow)

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
            dig = n % 10
            res += (dig ** 2)
            n //= 10
        
        return res