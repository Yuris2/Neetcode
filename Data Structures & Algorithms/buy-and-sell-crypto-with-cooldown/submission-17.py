class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #After you sell a coin, you cannt buy another on the next day
        #You can only own one coint at a time (i.e buy once can't sell)

        cache = {}

        def dp(i,sell):
            if i >= len(prices):
                return 0
            if (i, sell) in cache:
                return cache[(i,sell)]
            
            res = max(dp(i + 1, True) - prices[i], dp(i + 1, sell))
            if sell:
                res = max(dp(i + 2, False) + prices[i], res)

            cache[(i,sell)] = res
            return res
        
        return dp(0, False)


        #Brute Force
            #Each index, we have three options
                #Buy Coin (- to the total profit)
                #Sell Coin (if a buy was present, + total profit)
                #Skip Coin
            
            #With these three options, return the max from trying each index
                

