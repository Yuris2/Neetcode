class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache  = {}
        def dp(total):
            if total == 0:
                return 0
            if total in cache:
                return cache[total]
            if total < 0:
                return 2e9
            
            res = 2e9
            #We try each coin
            for c in coins:
                #If our target - coin > 0:
                if total - c >= 0:
                    res = min(1 + dp(total - c), res)
                    cache[total] = res
                    #We have used one coin, continue the subproblem
            
            return res
        
        res = dp(amount)
        if res < 2e9:
            return res
        return -1
        