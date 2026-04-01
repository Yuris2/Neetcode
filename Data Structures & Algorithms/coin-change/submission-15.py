class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dp(total):
            if total == 0:
                return 0
            if total in cache:
                return cache[total]

            count = 2e9

            for c in coins:
                if (total - c) >= 0:
                    count = min(count, 1 + dp(total - c))
            
            cache[total] = count
            return count
        
        res = dp(amount)
        if res < 2e9:
            return res
        return -1

        