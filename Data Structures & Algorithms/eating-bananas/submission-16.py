class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = 1
        maxSpeed = max(piles)
        res = maxSpeed

        while minSpeed <= maxSpeed:
            k = (minSpeed + maxSpeed) // 2
            time = 0

            for p in piles:
                time += math.ceil(p / k)
            
            if time > h:
                minSpeed = k + 1
            else:
                res = k
                maxSpeed = k - 1
        
        return res
        