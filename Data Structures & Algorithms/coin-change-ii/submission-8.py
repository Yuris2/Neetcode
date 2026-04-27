class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dp(i,total):
            if total == amount:
                return 1
            if i >= len(coins) or total > amount:
                return 0
            if (i,total) in cache:
                return cache[(i,total)]

            c1 = dp(i, total + coins[i])
            c2 = dp(i + 1, total)

            cache[(i,total)] = c1 + c2

            return c1 + c2
        
        return dp(0,0)
        