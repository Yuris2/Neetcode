import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for start, end, cost in flights:
            adjList[start].append((cost, end))
        
        seen = {}
        minHeap = [(0,src,k + 1)]

        while minHeap:
            cost, airport, stops = heapq.heappop(minHeap)

            if airport == dst:
                return cost
            if airport in seen and seen[airport] > stops:
                continue
            
            seen[airport] = stops

            for c, d in adjList[airport]:
                if stops != 0:
                    heapq.heappush(minHeap, (cost + c, d, stops - 1))
        
        return -1

        