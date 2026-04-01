class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfDigits(n)

        #Eventually going to be caught up to each other
        while slow != fast:
            slow = self.sumOfDigits(slow)
            fast = self.sumOfDigits(self.sumOfDigits(fast))

        #If they got stuck at 1 (Happy Number)
        if slow == 1 and fast == 1:
            return True
        else:
            #Stuck at non-one (False)
            return False
            

    
    def sumOfDigits(self,n):
        res = 0
        while n:
            digit = n % 10
            res += (digit ** 2)
            n = n // 10
        
        return res

            
        