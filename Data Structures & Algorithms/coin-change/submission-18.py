class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dp(total):
            if total == 0:
                return 0
            if total in cache:
                return cache[total]
            
            res = 2e9
            for c in coins:
                if total - c >= 0:
                    res = min(res, 1 + dp(total - c))
            
            cache[total] = res
            return res
        
        r = dp(amount)

        if r < 2e9:
            return r
        else:
            return -1

        