class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = 1
        res = maxSpeed = max(piles)

        while minSpeed <= maxSpeed:
            k = (maxSpeed + minSpeed) // 2
            time = 0

            for p in piles:
                time += math.ceil(p / k)
            
            if time <= h:
                res = k
                maxSpeed = k - 1
            else:
                minSpeed = k + 1
        
        return res
                
      

        