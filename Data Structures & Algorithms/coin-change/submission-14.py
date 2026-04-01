class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dp(amount):
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            
            res = 2e9
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dp(amount - c))
            
            cache[amount] = res
            return res
        
        ans = dp(amount)

        return ans if ans < 2e9 else -1


        