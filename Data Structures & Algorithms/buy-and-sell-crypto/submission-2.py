class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            profit = prices[sell] - prices[buy]

            res = max(res, profit)

            if profit < 0:
                buy = sell
            
            sell +=1
        
        return res
        