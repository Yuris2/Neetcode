class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(total):
            if total == 0:
                return 0
            if total in cache:
                return cache[total]
            
            res = 2e9 
            for c in coins:
                if total - c >= 0:
                    res = min(res, 1 + dfs(total - c))
            
            cache[total] = res
            return res
        
        ans = dfs(amount)
        if ans < 2e9:
            return ans
        else:
            return -1

        