class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        buy = 0
        sell = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]

            if profit < 0:
                buy = sell

            maxPro = max(maxPro, profit)
            sell += 1
        
        return maxPro

            
        
        