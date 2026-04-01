class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.res = 1e9
        cache = {}
        def backtrack(amount):
            if amount == 0:
                return 0
            
            if amount in cache:
                return cache[amount]
            
            res = 1e9
            for coin in coins:
                if (amount - coin) >= 0:
                    res = min(res,1 + backtrack(amount - coin))
                    
            cache[amount] = res
            return res
            
        
        minc = backtrack(amount)
        if minc >= 1e9:
            return -1
        else:
            return minc
        
        