import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2
            t = 0

            for p in piles:
                t += math.ceil(p / k)
            
            if t > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        
        return res
                
        