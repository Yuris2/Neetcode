class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cur = [0,0]
        prev = [0,0]
        cooldown = [0,0]
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for sell in range(1, -1, -1):
                #Sell
                if sell == 1:
                    cd = cooldown[0] if i + 2 <= n else 0
                    #Sell at different point, compare to cooldown
                    cur[sell] = max(prev[sell], cd + prices[i]) 
                #Buy
                else:
                    #Buy a coin or skip the buy
                    cur[sell]  = max(prev[1] - prices[i], prev[0])
                
            tmp1, tmp2 = cur, prev
            cooldown, prev = tmp2, tmp1
            cur = [0,0]
        
        return prev[0]

        