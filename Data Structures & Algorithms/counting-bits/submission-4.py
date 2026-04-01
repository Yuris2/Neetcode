class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offSet = 1

        for i in range(1, n + 1):
            if i == offSet * 2:
                offSet *= 2
            dp[i] = 1 + dp[i - offSet]
        
        return dp
        