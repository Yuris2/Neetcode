class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        

        for i in range(n - 1, -1, -1):
            dp[i][amount] = 1
            for total in range(amount - 1, -1, -1):
                if total + coins[i] <= amount:
                    dp[i][total] += dp[i][total + coins[i]]
                dp[i][total] += dp[i + 1][total]
        
        return dp[0][0]
