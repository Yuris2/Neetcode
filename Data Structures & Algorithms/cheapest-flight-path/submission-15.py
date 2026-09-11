import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for s,d,cost in flights:
            adjList[s].append((d,cost))
        
        heap = [(0, k + 1, src)]
        seen = {}

        while heap:
            cost, rem, air = heapq.heappop(heap)

            if air == dst:
                return cost
            if air in seen and seen[air] > rem:
                continue
            
            seen[air] = rem

            for d,c in adjList[air]:
                if rem > 0:
                    total = c + cost
                    heapq.heappush(heap, (total, rem - 1, d))
        
        return -1

        