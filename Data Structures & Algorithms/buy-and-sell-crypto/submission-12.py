class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 1

        while r < len(prices):
            diff = prices[r] - prices[l]
            if diff < 0:
                l = r
            elif diff > maxProfit:
                maxProfit = diff
            r += 1
        
        return maxProfit
                
                
        