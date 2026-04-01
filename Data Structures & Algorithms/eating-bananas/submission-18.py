import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            timeToEat = 0
            for p in piles:
                timeToEat += math.ceil(p / m)
            
            if timeToEat <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res






        