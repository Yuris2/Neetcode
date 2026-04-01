class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy, sell = 0, 1

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            maxProfit = max(maxProfit, profit)

            #if there is a dip
            if profit < 0:
                buy = sell
            
            sell += 1
        
        return maxProfit


        