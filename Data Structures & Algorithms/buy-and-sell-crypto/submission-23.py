class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = 0

        for sell in range(len(prices)):
            profit = prices[sell] - prices[buy]

            res = max(res, profit)

            if profit < 0:
                buy = sell
        
        return res

        
        
        