import collections
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #Pattern
            #Constructing a Minimum Spanning Tree
        
        #General Idea
            #Use algo to constuct MST
            #Use a Heap to track the min cost via manhattan distance
            #Use a set to track nodes you have seen
            #Return total Cost
        
        heap = [(0, points[0][0], points[0][1])]
        seen = set()
        res = 0

        while heap:
            cost, xi, yi = heapq.heappop(heap)

            if (xi,yi) in seen:
                continue 
            
            seen.add((xi,yi))
            res += cost

            for xj, yj in points:
                if (xj, yj) not in seen:
                    manhattan = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(heap, (manhattan, xj, yj))
        
        return res

        