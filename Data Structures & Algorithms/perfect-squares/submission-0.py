import math
class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}
        def dp(target):
            if target == 0:
                return 0
            if target in cache:
                return cache[target]
            res = 2e9
            for num in range(1, int(math.sqrt(target)) + 1):
                square = num * num

                if target - square >= 0:
                    res = min(res, 1 + dp(target - square))
            
            cache[target] = res
                
            return res
        
        return dp(n)

        