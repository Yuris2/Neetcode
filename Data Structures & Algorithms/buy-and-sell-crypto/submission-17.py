class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        res = 0
        
        for sell in range(1,len(prices)):
            profit = prices[sell] - prices[buy]

            if profit > 0:
                res = max(profit, res)
            else:
                #We found a new minimum/buying point
                buy = sell
        
        return res
