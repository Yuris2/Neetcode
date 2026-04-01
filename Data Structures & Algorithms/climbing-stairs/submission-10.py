class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        res = [1, 2]

        for i in range(3, n + 1):
            tmp = res[1]
            res[1] = res[0] + res[1]
            res[0] = tmp
        
        return res[1]
        

        