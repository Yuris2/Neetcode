import math
class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}
        def dp(total):
            if total == 0:
                return 0
            if total in cache:
                return cache[total]
            res = 2e9
            for num in range(1, int(math.sqrt(total)) + 1):
                square = num * num

                if total - square >= 0:
                    res = min(res, 1 + dp(total - square))
                    
            cache[total] = res
            return res
            
        return dp(n)


        