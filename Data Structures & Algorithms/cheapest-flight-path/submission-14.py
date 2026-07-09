import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for s,d,c in flights:
            adjList[s].append((d,c))
        
        heap = [(0,src,k + 1)]

        #Airport = num stops
        seen = {}

        while heap:
            c,a,r = heapq.heappop(heap)

            if a == dst:
                return c
            if a in seen and seen[a] > r:
                continue
            
            seen[a] = r

            for dest, cost in adjList[a]:
                if r != 0:
                    heapq.heappush(heap, (c + cost, dest, r - 1))
        
        return -1


        