class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        cur = [0] * (amount + 1)
        prev = [0] * (amount + 1)
        
        for i in range(n - 1, -1, -1):
            cur[amount] = 1
            
            for total in range(amount - 1, -1, -1):
                #c1
                if total + coins[i] <= amount:
                    cur[total] = cur[total + coins[i]]
                #c2
                cur[total] += prev[total]
            
            prev = cur
            cur = [0] * (amount + 1)
        
        return prev[0]