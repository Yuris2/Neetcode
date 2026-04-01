class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = max(piles)

        while l <= r:
            m = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / m)
            
            if time > h:
                l = m + 1
            else:
                res = m
                r = m - 1
        
        return res
        