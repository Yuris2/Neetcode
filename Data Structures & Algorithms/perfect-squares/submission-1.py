import math
class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}
        def dp(amount):
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            
            res = 2e9
            for num in range(1, int(math.sqrt(amount)) + 1):
                square = num * num
                if amount - square >= 0:
                    res = min(res, 1 + dp(amount - square))
            
            cache[amount] = res
            return res
        
        return dp(n)

        