class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n != 0:
            dig = n & 1
            if dig == 1:
                res += 1
            n >>= 1
        
        return res

            
