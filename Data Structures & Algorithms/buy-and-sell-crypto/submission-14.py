class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i, j = 0, 1
        while j < len(prices):
            delta = prices[j] - prices[i]
            if delta < 0:
                i = j
            else:
                if delta > profit:
                    profit = delta
            j += 1
        return profit
        