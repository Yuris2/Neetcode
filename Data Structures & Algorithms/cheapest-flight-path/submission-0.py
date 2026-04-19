import collections
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #Try to find the cheapest (shortest) flight from src to dst within k stops
            #Djikstras because of shortest path (with weight)
        
        #Solution Intuition
            #Modified Version of Djikstras except now we have to deal with steps remaining
                #Instead of just checking if a node is seen
                    #We have to see if the revisiting the node results in more available steps
                #When adding neighbors onto the heap
                    #Also have to ensure that we have enough stops available (k > 0)
            #Min Heap with dst guarantees the cheapest cost (cost, node, steps_remaining)
            #Return -1 if we never reach the end
        
        #Constructing the adjList
        adjList = defaultdict(list)
        for fr, to, price in flights:
            adjList[fr].append((to, price))
        
        #Min Heap starting with k steps remaining
        minHeap = [(0,src,k + 1)]
        #airport: steps remaining
        seen = defaultdict(int)

        while minHeap:
            cost, airport, steps = heapq.heappop(minHeap)

            #If we hit the destination
            if airport == dst:
                return cost
            #Checking if it can even end up in valid solution
            if airport in seen and seen[airport] > steps:
                continue
            
            seen[airport] = steps

            for out, c in adjList[airport]:
                if steps != 0:
                    heapq.heappush(minHeap, (cost + c, out, steps - 1))

        #We will never reach the end 
        return -1

        