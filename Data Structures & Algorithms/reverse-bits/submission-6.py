class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            res <<= 1
            digit = n & 1
            res += digit
            n >>= 1
        
        return res

        