class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            delta = prices[r] - prices[l]
            if delta < 0:
                l = r
            elif delta > max_profit:
                max_profit = delta
            r += 1
        return max_profit