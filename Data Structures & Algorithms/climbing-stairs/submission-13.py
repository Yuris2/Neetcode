class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        cache = [1, 1]
        while n > 1:
            new = cache[0] + cache[1]
            cache[0] = cache[1]
            cache[1] = new
            n -= 1
        
        return cache[1]

