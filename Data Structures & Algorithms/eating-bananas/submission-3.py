

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Think about the brute force solution
        #we can try a rate of 1,2,3.... until we find the minimum
        #however, if k can't finish in 3, no way he can finish in 2
        #if koko eats at the max height to finish, guarantee to finish everything
        #minimum eating speed is 1 banana per hour
        # run a BS to make it more efficient

        l = 1
        r = max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            time = 0

            for p in piles:
                time += math.ceil(p / m)
            
            if time <= h:
                r = m - 1
                res = m
            elif time > h:
                l = m + 1
            
        
        return res
        

        