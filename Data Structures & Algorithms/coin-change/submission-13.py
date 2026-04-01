class Solution:
    def coinChange(self, coins: List[int], coin: int) -> int:
        cache = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            
            res = 2e9
            for c in coins:
                if amount - c >= 0:
                    res = min(res, 1 + dfs(amount - c))
            
            cache[amount] = res
            
            return res
        
        ans = dfs(coin)
        if ans < 2e9:
            return ans
        else:
            return -1
        