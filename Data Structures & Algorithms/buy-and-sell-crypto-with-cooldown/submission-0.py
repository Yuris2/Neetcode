class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Buy and sell one coin multiple times s.t 
            #you can't buy and sell the coin on the same day
            #after you sell, you cannot buy for one day
            #only own one coin at a time
                #Have to follow a buy, sell pattern
        
        #Return maxProfit you can achieve

        cache = {}
        def dp(i, sell):
            if i >= len(prices):
                return 0
            if (i, sell) in cache:
                return cache[(i, sell)]
            
            res = 0
            #Choices
                #Buy current coin and skip (buying is a neg contr)
            res = max(dp(i + 1, True) - prices[i], dp(i + 1, sell))
            
            if sell:
                #Selling contributes by prices[i]
                res = max(res, prices[i] + dp(i + 2, False))
            cache[(i, sell)] = res
            return res
            
        return dp(0,False)

        