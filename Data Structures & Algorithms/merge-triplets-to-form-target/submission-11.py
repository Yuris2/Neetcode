class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t1,t2,t3 = target
        res = [False, False, False]

        for a,b,c in triplets:
            if a > t1 or b > t2 or c > t3:
                continue
            
            if a == t1:
                res[0] = True
            if b == t2:
                res[1] = True
            if c == t3:
                res[2] = True
        
        for r in res:
            if not r:
                return False
        
        return True