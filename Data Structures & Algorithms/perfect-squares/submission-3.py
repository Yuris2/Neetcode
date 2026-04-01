import math
class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}
        def perfectSquare(num):
            if num == 0:
                return 0
            if num == 1:
                return 1
            if num in cache:
                return cache[num]
            
            res = 2e9
            for i in range(1, int(math.sqrt(num)) + 1):
                square = i * i
                res = min(res, 1 + perfectSquare(num - square))
            
            cache[num] = res
            return res
        
        return perfectSquare(n)

