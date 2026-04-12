class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dp(i, total):
            if total == amount:
                return 1 
            if total > amount or i >= len(coins):
                return 0
            if (i, total) in cache:
                return cache[(i, total)]

            #Use coin at i and maybe use it again
            c1 = dp(i, total + coins[i])
            #Skip coin at i and never use it again
            c2 = dp(i + 1, total)

            cache[(i, total)] = c1 + c2
            return c1 + c2
        
        return dp(0,0)
        