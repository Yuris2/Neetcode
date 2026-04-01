class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Backtracking
        #Try every possible combination of coins
        cache = {}

        def backtrack(total):
            if total == 0:
                return 0
            if total in cache:
                return cache[total]
            
            res = 2e9

            for c in coins:
                if total - c >= 0:
                    res = min(res, 1 + backtrack(total - c))
            
            cache[total] = res
            return res
        
        res = backtrack(amount)
        if res < 2e9:
            return res
        else:
            return -1

        