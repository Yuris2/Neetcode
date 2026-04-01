class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False, False, False]

        t1, t2, t3 = target

        for v1, v2, v3 in triplets:
            if v1 > t1 or v2 > t2 or v3 > t3:
                continue
            
            if v1 == t1:
                res[0] = True
            if v2 == t2:
                res[1] = True
            if v3 == t3:
                res[2] = True
        
        for r in res:
            if not r: 
                return False
        
        return True
        