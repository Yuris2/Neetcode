import math
class Solution:
    def numSquares(self, num: int) -> int:
        cache = {}
        def dp(n):
            if n <= 1:
                return n
            if n in cache:
                return cache[n]
            
            sqrt = n ** 0.5

            res = 2e9
            for i in range(1, int(sqrt) + 1):
                square = i * i
                if n - square >= 0:
                    res = min(res, 1 + dp(n - square))
            
            cache[n] = res
            return res
        
        return dp(num)
                
            
            
        