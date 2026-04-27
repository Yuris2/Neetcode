import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for dep, arr, cost in flights:
            adjList[dep].append((cost, arr))
        
        minHeap = [(0,src,k + 1)]
        #Airport:Cost
        seen = {}

        while minHeap:
            cost, airport, remaining = heapq.heappop(minHeap)

            if airport == dst:
                return cost
            if airport in seen and seen[airport] > remaining:
                continue
            
            seen[airport] = remaining
            for c, d in adjList[airport]:
                if remaining != 0:
                    heapq.heappush(minHeap, (c + cost, d, remaining - 1))
        
        return -1
            

        
        