class Solution:
    def climbStairs(self, n1: int) -> int:
        if n1 <= 2:
            return n1
        
        #Steps 1 and 2
        n = [1,2]

        for i in range(3, n1 + 1):
            tmp = n[1]
            n[1] = n[0] + n[1]
            n[0] = tmp
        
        return n[1]