import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # highest rate you can try is max(piles)
        res = max(piles)

        # between 1 and max(piles) you are trying for a min
        l, r = 1, max(piles)
        while l <= r:
            # k (try rate)
            k = (l + r) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours > h:
                l = k + 1
            
            else:
                res = min(res, k)
                r = k - 1

        return res