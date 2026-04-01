class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        cache[0] = 1
        cache[1] = 1
        x = 2
        while x <= n:
            cache[x] = cache[x - 1] + cache[x - 2]
            x += 1
        return cache[x - 1]