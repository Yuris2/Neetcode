'''
You are given an integer array prices where prices[i] is the 
price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin 
and choose a different day in the future to sell it.

Return the maximum profit you can achieve. 
You may choose to not make any transactions, in which case the profit would be 0.

#prices = [10,1,5,6,7,1]
# Max profit = 6 (7 - 1) 
# Selling Point has to be on the right of the array



'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Keep Track of Our Max Profit (Start at 0)
        maxProfit = 0
        buy, sell = 0, 1

        #Sell > Buy
        #Keep track of the price that we buy, and the price that we sell
        while sell < len(prices):
            profit = prices[sell] - prices[buy]

            if profit < 0:
                buy = sell
            
            maxProfit = max(maxProfit, profit)

            sell += 1

            #Move our sell point to the right of the array
            #If want to move our buy point when our sell point < buy point
            #Calculate our max profit from sell - buy
        
        return maxProfit
        #Return the max profit


        