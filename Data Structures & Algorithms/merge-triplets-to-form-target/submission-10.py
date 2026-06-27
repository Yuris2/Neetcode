class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t1,t2,t3 = target
        res = [False, False, False]

        for x,y,z in triplets:
            if x > t1 or y > t2 or z > t3:
                continue

            if x == t1:
                res[0] = True
            if y == t2:
                res[1] = True
            if z == t3:
                res[2] = True

        for r in res:
            if not r:
                return False

        return True        