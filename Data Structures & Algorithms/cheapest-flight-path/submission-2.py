import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for dep, arr, cost in flights:
            adjList[dep].append((arr, cost))
        
        minHeap = [(0,src, k + 1)]
        seen = {}

        while minHeap:
            totalCost, airport, stops = heapq.heappop(minHeap)

            if airport == dst:
                return totalCost
            if airport in seen and seen[airport] > stops:
                continue
            
            seen[airport] = stops

            for out, cost in adjList[airport]:
                if stops != 0:
                    heapq.heappush(minHeap, (totalCost + cost, out, stops - 1))
        
        return -1
        
        