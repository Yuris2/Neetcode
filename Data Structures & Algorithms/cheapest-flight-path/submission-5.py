import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for fr, to, price in flights:
            adjList[fr].append((to, price))
        
        minHeap = [(0, src, k + 1)]
        seen = {}

        while minHeap:
            cost, airport, remaining = heapq.heappop(minHeap)

            if airport == dst:
                return cost
            if airport in seen and seen[airport] > remaining:
                continue
            
            seen[airport] = remaining

            for outbound, c in adjList[airport]:
                if remaining != 0:
                    heapq.heappush(minHeap, (cost + c, outbound, remaining - 1))
        
        return -1
        