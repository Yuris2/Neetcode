class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        #Two pointers
        buy = 0
        sell = 1

        while sell < len(prices):
            profit = prices[sell] - prices[buy]

            res = max(profit , res)
            
            if profit < 0:
                buy = sell
            
            sell +=1
        
        return res
        
        