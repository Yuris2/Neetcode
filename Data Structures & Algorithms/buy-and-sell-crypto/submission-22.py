class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0,0
        res = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            res = max(profit, res)

            if profit < 0:
                buy = sell
            
            sell += 1
        
        return res
        