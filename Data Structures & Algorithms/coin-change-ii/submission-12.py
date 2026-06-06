class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #Pattern
            #2D DP - 2 choice
        #General Idea
            #Either add current coin to running total or skip
            #If total = amount we have found a possibility
            #DP[total] = number of ways we can add the coins to get to this total
        
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        #Iterating through all the coins backwards
        for i in range(n - 1, -1, -1):
            #Because we have reached the desired amount
            dp[i][-1] = 1
            for total in range(amount - 1, -1, -1):
                if total + coins[i] <= amount:
                    dp[i][total] += dp[i][total + coins[i]]
                dp[i][total] += dp[i + 1][total]
        
        return dp[0][0]
        