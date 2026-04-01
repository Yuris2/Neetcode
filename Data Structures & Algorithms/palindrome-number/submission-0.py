class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        
        revNum = 0
        cpy = x

        while cpy > 0:
            dig = cpy % 10
            revNum = (revNum * 10) + dig
            cpy = cpy // 10
        
        return revNum == x