class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,res = 0,0
        for r in range(len(prices)):
            res = max(prices[r]-prices[l],res)
            if prices[r] < prices[l]: l = r
        return res

        