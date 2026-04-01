class Solution:
    def isHappy(self, n: int) -> bool:
        #Sum of the square of its digits
        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.sumOfDigits(n)
            if n == 1:
                return True
        
        return False
            

    
    def sumOfDigits(self,n):
        res = 0
        while n:
            digit = n % 10
            res += (digit ** 2)
            n = n // 10
        
        return res

            
        