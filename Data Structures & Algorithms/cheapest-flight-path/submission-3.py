import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for start, dest, cost in flights:
            adjList[start].append((dest, cost))
        
        minHeap = [(0, src, k + 1)]
        seen = {}

        while minHeap:
            cost, airport, steps = heapq.heappop(minHeap)

            if airport == dst:
                return cost
            if airport in seen and seen[airport] > steps:
                continue
            
            seen[airport] = steps

            for dest, c in adjList[airport]:
                if steps != 0:
                    heapq.heappush(minHeap, (cost + c, dest, steps - 1))

        return -1

        