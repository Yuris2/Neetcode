class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def backtrack(amount):
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            
            res = 1e9
            for c in coins:
                if (amount - c >= 0):
                    res = min(res, 1 + backtrack(amount - c))
            cache[amount] = res
            return res
        
        minCoins = backtrack(amount)

        if minCoins < 1e9:
            return minCoins
        else:
            return -1


        
        