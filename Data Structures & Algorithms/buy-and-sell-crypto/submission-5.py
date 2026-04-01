class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1

        res = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]

            if profit < 0:
                buy = sell
            
            res = max(res, profit)

            sell += 1
        
        return res
        