import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [2e9] * (n + 1)
        dp[0], dp[1] = 0,1

        for i in range(1, n + 1):
            square_root = int(math.sqrt(i))

            for root in range(1, square_root + 1):
                square = root * root
                if i - square >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - square])
        
        return dp[n]
    

        