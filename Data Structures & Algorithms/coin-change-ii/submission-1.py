class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        i = len(coins)

        #dp[i]
        prev = [0] * (amount + 1)
        
        cur = [0] * (amount + 1)

        #Whenver you reach amount, there is only 1 way to complete
        #Do nothing
        prev[amount] = 1

        for i in range(i - 1, -1, -1):
            cur[amount] = 1
            for total in range(amount - 1, -1, -1):
                #Use coin[i]
                if total + coins[i] <= amount:
                    cur[total] = cur[total + coins[i]]
                #Skip coin[i] and never use it again
                cur[total] += prev[total]
            
            prev = cur
            cur = [0] * (amount + 1)
        
        return prev[0]
            
        