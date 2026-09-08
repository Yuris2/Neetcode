class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dp(i, sell):
            if i >= len(prices):
                return 0
            if (i, sell) in cache:
                return cache[(i,sell)]

            total = 0

            if sell:
                total = max(total, dp(i + 2, False) + prices[i])
            
            total = max(total, dp(i + 1, True) - prices[i], dp(i + 1, sell))
            cache[(i,sell)] = total
            return total
        
        return dp(0, False)



