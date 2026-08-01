class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}
        def dp(num):
            if num <= 1:
                return num
            if num in cache:
                return cache[num]
            
            res = 2e9

            for n in range(int(math.sqrt(num)), 0, -1):
                square = n * n
                res = min(res, 1 + dp(num - square))

            cache[num] = res
            return res
        
        return dp(n)

        