class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        #Only do it 32 times
        for i in range(32):
            #Prepare res 
            res <<= 1
            bit = n & 1
            n >>= 1
            res += bit
        
        return res
        