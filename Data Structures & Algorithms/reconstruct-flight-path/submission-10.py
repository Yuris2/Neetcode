#Originally Departed from JFK
#If multiple valid flights, return one with lexical smaller order
#Have to take every edge and condense it
    #Eulerian Path
import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)

        for src, dst in tickets:
            heapq.heappush(adjList[src], dst)
        
        res = []
        def dfs(airport):
            if not airport:
                return
            
            while adjList[airport]:
                dest = heapq.heappop(adjList[airport])
                dfs(dest)

            res.append(airport)
        
        dfs("JFK")
        res.reverse()
        return res

        