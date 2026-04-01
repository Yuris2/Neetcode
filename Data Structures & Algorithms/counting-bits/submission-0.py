class Solution:
    def countBits(self, n: int) -> List[int]:
        #Recognize the pattern
        #The number of 1 bits = 1 + dp[n - MSB we reached]
        dp = [0] * (n + 1)
        msb = 1

        #We start at 1, because our BC is already 0
        for i in range(1,n + 1):
            if i == (msb * 2):
                msb = i
            dp[i] = 1 + dp[i - msb]
        
        return dp



        