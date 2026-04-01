class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = 0


        for r in range(len(prices)):
            profit = prices[r] - prices[buy]

            res = max(profit, res)
            if profit < 0:
                buy = r
        
        return res
            
            
        