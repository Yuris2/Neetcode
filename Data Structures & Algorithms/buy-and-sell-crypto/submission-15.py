class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            cur = prices[r] - prices[l]
            if cur < 0:
                l = r
            else:
                if cur > maxProfit:
                    maxProfit = cur
            r += 1
        return maxProfit