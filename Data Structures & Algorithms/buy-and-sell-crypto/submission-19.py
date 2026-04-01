class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        res = 0

        for sell in range(len(prices)):
            profit = prices[sell] - prices[buy] 

            res = max(profit, res)

            if profit < 0:
                buy = sell
        
        return res
        