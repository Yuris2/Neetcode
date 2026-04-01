class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            #Make room for the incoming bit
            res <<= 1
            #Extract the bit from n
            bit = n & 1
            #Shift n by 1
            n >>= 1
            #Add bit to res (can do res | bit)
            res += bit

        
        return res