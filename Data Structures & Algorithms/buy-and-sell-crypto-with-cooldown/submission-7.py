class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Depends on sell and next row
        cur = [0,0]
        prev = [0,0]
        cooldown = [0,0]

        #Sell = True/1 | Buy = False/0
        for i in range(len(prices) - 1, -1, -1):
            for sell in range(1,-1,-1):
                if sell == 1:
                    profit = cooldown[0] + prices[i]
                    cur[sell] = max(prev[1], profit)
                else:
                    c1 = prev[1] - prices[i]
                    c2 = prev[0]
                    cur[sell] = max(c1, c2)
            cooldown = prev
            prev = cur
            cur = [0,0]
        
        return prev[0]