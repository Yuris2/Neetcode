class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 0
        maxProfit = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]

            if profit < 0:
                buy = sell
            
            maxProfit = max(profit, maxProfit)
            sell += 1
        
        return maxProfit
            
        