import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #Pattern
            #Djikstras tracking cost and set tracking max number of stops
        
        #General Idea
            #Create an adj list between airports
            #Run djikstras at the starting airport, using a set that tracks
            #airport and max number of stops as seen
            #Return cost if airport == dst
        
        adjList = defaultdict(list)

        for s,d,c in flights:
            adjList[s].append((d,c))
        
        heap = [(0,src, k + 1)]
        seen = {}

        while heap:
            cost, airport, stops = heapq.heappop(heap)

            if airport == dst:
                return cost
            if airport in seen and seen[airport] > stops:
                continue
            
            seen[airport] = stops

            for adj, c in adjList[airport]:
                if stops != 0:
                    heapq.heappush(heap, (c + cost, adj, stops - 1))

        return -1

        
        