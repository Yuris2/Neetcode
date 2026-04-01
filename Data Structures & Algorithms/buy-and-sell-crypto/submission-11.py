class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        r = 1
        while r < len(prices):
            delta = prices[r] - prices[l]
            if delta < 0:
                l = r
            else:
                if delta > max_profit:
                    max_profit = delta
            r += 1
        return max_profit
        